import os
from datetime import datetime, date
import re
import magic
from hashlib import md5
import numpy
import simplejson as json
from decimal import Decimal
from bson.decimal128 import Decimal128
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from zipfile import ZipFile
import shutil
from pathlib import Path

import settings


def get_today():
	return date.today().strftime("%Y%m%d")


def calc_etag(inputfile, partsize=0):
	if not partsize:
		partsize = os.path.getsize(inputfile)
	md5_digests = []
	with open(inputfile, 'rb') as f:
		for chunk in iter(lambda: f.read(partsize), b''):
			md5_digests.append(md5(chunk).digest())
	return md5(b''.join(md5_digests)).hexdigest() + '-' + str(len(md5_digests))


def calc_etag_binary(binary):
    md5_digests = []
    md5_digests.append(md5(binary).digest())
    return md5(b''.join(md5_digests)).hexdigest() + '-' + str(len(md5_digests))


def get_content_type(path):
	mime = magic.Magic(mime=True)
	return mime.from_file(path)


def get_last_modified(url):
	r = requests.head(url)
	url_date_str = r.headers['last-modified']
	url_date_obj = datetime.strptime(url_date_str, '%b %d %Y %I:%M%p')
	return url_date_obj


def get_key_with_value_in_dict(value, dict_obj):
	key = None
	key_list = list(dict_obj.keys())
	val_list = list(dict_obj.values())
	if value in val_list:
		position = val_list.index(value)
		key = key_list[position]
	return key


def get_key_list_in_map_by_value(value, dict_obj):
	key_list = list(dict_obj.keys())
	val_list = list(dict_obj.values())
	result = [key_list[i] for i, x in enumerate(val_list) if x == value]
	return result


def validate_str_data(data):
	result = ''
	if data:
		result = data.strip()
	return result


def extract_numbers_in_str(params: str):
    re_list: list[str] = re.findall('-?[0-9]+\.[0-9]*|-?\.[0-9]*|-?[0-9]+/[0-9]*|-?[0-9]+', params)
    num_list = []
    for val in re_list:
        if val.startswith('.'):
            num_list.append(val.replace('.', ''))
        elif val.find('/') > 0:
            spl_list = val.split('/')
            value = int(spl_list[0]) / int(spl_list[1])
            num_list.append(value)
        else:
            num_list.append(val)
    num_list = [num for num in num_list if num != ""]

    def convert_num(str_val):
        str_val = str_val.replace('.0', '')
        reg = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
        result = reg.match(str_val)
        if result:
            return float(str_val)
        else:
            return int(str_val)

    result_list = list(map(convert_num, num_list))
    if len(result_list) > 0:
        return result_list[0]

    return 0


def validate_numeric_data(data):
    result = 0
    if data:
        try:
            result = float(data)
        except ValueError:
            result = extract_numbers_in_str(data)

    return result


def validate_int_data(data):
    result = 0
    if data:
        try:
            result = int(data)
        except ValueError:
            result = extract_numbers_in_str(data)

    return result


def get_utc_date(str_date, date_format):
	if str_date:
		date_data = datetime.strptime(str_date, date_format)
		if date_data:
			return datetime.utcfromtimestamp(date_data.timestamp())
	return None


def extract_float_in_string(param):
	result = re.sub(r"[^\d.]", '', param)
	return float(result)


def convert_dict_json(value):
	return json.dumps(value, cls=DecimalEncoder)


def convert_decimal128(param):
	if param is None or not isinstance(param, dict):
		return None

	dict_item=param.copy()

	for k, v in list(dict_item.items()):
		if isinstance(v, dict):
			convert_decimal128(v)
		elif isinstance(v, list):
			for l in v:
				convert_decimal128(l)
		elif isinstance(v, Decimal):
			dict_item[k] = Decimal128(str(v))

	return dict_item


def convert_decimal(dict_item):
    if dict_item is None: return None

    for k, v in list(dict_item.items()):
        if isinstance(v, dict):
            convert_decimal(v)
        elif isinstance(v, list):
            for l in v:
                convert_decimal(l)
        elif isinstance(v, Decimal128):
            dict_item[k] = Decimal(str(v))

    return dict_item


def get_response(url, domain):
	result = None

	session = requests.Session()
	retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 500, 502, 503, 504 ])
	session.mount(domain, HTTPAdapter(pool_connections=100, pool_maxsize=100, max_retries=retries))

	try:
		result = session.get(url)
	except Exception as e:
		print(str(e))
		return None

	return result


def download_file(url, download_folder_path, file_name):
    isExist = os.path.exists(download_folder_path)
    if not isExist:
        os.makedirs(download_folder_path)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    full_path = download_folder_path + file_name
    if response.status_code == 200:
        with open(full_path, 'wb') as f:
            f.write(response.content)
        return full_path
    else:
        return None


def extract_all_in_zip(zip_file_path, extract_path):
	zf = ZipFile(zip_file_path)
	zf.extractall(extract_path)


def create_range_dict(begin_num, begin_str, end_num, end_str, step, step_str,step_end_str=''):
    range_dict = {
        begin_num: begin_str,
        end_num: end_str
    }
    for num in numpy.arange(begin_num, end_num, step):
        range_dict[num] = f'{num} {step_str} {num + step}{step_end_str}'
    return range_dict


def find_range_result(val,begin_num, begin_str, end_num, end_str, step, step_str,step_end_str=''):
    range_dict = create_range_dict(begin_num, begin_str, end_num, end_str, step, step_str,step_end_str)
    if isinstance(step,int) or isinstance(step,float):
        final_num = int(val/step)*step
    else:
        return None
    if final_num < begin_num:
        return begin_str
    elif final_num > end_num:
        return end_num
    else:
        return range_dict[final_num]
    

def find_range_and_index(val,begin_num, begin_str, end_num, end_str, step, step_str,step_end_str=''):
    result = {}
    range_dict = create_range_dict(begin_num, begin_str, end_num, end_str, step, step_str,step_end_str)
    if isinstance(step,int) or isinstance(step,float):
        final_num = int(val/step)*step
    
        boundaries = sorted(range_dict.keys())

        if final_num < begin_num:
            range_index = 0
            result['id'] = range_index
            result['range'] = begin_str        
        elif final_num > end_num:
            range_index = len(boundaries) - 1
            result['id'] = range_index
            result['range'] = end_num
        else:
            range_index = boundaries.index(final_num)
            result['id'] = range_index
            result['range'] = range_dict[final_num]

    return result


def download_picture(picture_file_name, image_folder='product_images/'):
    if 'haw' in settings.DB_CONFIG['env']:
        url = 'https://www.hawthorneonline.com/'
    else:
        url = 'https://www.abcwarehouse.com/'
    url += image_folder + picture_file_name
    try:
        return download_file(url, settings.WWWROOT_PRODUCT_IMAGES_DIR, picture_file_name)
    except:
        return None


def download_promo_picture(picture_file_name):
    return download_picture(picture_file_name, 'promo-product-square/')


def cmd_xcopy_file(src, dst):
    # Check the operating system and use the respective command
    if os.name == 'nt':  # Windows
        cmd = f'xcopy "{src}" "{dst}" /Y'
    else:  # Unix/Linux
        cmd = f'cp "{src}" "{dst}"'
    # Copy File
    os.system(cmd)


def copy_file(src, dst):
    shutil.copyfile(src, dst)


def move_file(src, dst):
    shutil.move(src, dst)
    

def move_dir(src, dst):
    shutil.move(src, dst)
    

def remove_folder(folder_path):
    shutil.rmtree(folder_path)


def same_picture_checking(image1, image2):
    import imagehash
    cutoff = 0.001  # maximum bits that could be different between the hashes.

    nop_pic_binary_hash = imagehash.average_hash(image1)
    stg_pic_binary_hash = imagehash.average_hash(image2)
    if stg_pic_binary_hash - nop_pic_binary_hash < cutoff: # if same image
        return True
    else:
        return False


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o, Decimal128):
            return float(o.to_decimal())
        return json.JSONEncoder.default(self, o)

