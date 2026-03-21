from .nop_sql import NopQuery
from .nop_data import NopData
from .core.db import AutoDao
from .core.utils import *
import os

from slugify import slugify


nop_dao = AutoDao("nop")

NopData.sku_pid_map = nop_dao.get_hashmap(NopQuery.GET_ALL_SKU_PID_SQL)
NopData.products_pub_del_tbl = nop_dao.get_hashtable(NopQuery.GET_ALL_PRODUCT_PUB_DEL_SQL)
NopData.categories = nop_dao.get_hashtable(NopQuery.GET_ALL_CATEGORY_SQL)
NopData.manufacturers = nop_dao.get_hashtable(NopQuery.GET_ALL_MANUFACTURER_SQL, key=1)
NopData.product_category_mappings = nop_dao.get_hashtable(NopQuery.GET_ALL_PRODUCT_CATEGORY_MAPPING_SQL)
NopData.picture_title_map = nop_dao.get_hashmap(NopQuery.GET_ALL_PICTURE_SQL)
NopData.product_picture_mapping_tbl = nop_dao.get_hashtable(NopQuery.GET_ALL_PRODUCT_PICTURE_MAPPING_SQL)


class NopTool:
    
    def reload_picture_maps():
        NopData.picture_title_map = nop_dao.get_hashmap(NopQuery.GET_ALL_PICTURE_SQL)
        NopData.product_picture_mapping_tbl = nop_dao.get_hashtable(NopQuery.GET_ALL_PRODUCT_PICTURE_MAPPING_SQL)
    
    def get_sku_from_pid(pid):
        if pid in NopData.products_pub_del_tbl.keys():
            return NopData.products_pub_del_tbl[pid]['Sku']

    def get_pid_from_sku(sku):
        if sku in NopData.sku_pid_map.keys():
            return NopData.sku_pid_map[sku]
                    
    def is_new_product(sku):
        result = False

        if NopData.sku_pid_map:
            if sku not in NopData.sku_pid_map.keys():
                result = True
        else:
            result = True

        return result

    def get_product_by_id(pid):
        product = nop_dao.get_one_row_dict(NopQuery.GET_PRODUCT_BY_ID_SQL, pid)
        return product
        
    def insert_product(param):
        insert_col_list = getattr(NopQuery, f"INSERT_COLUMN_LIST_{os.environ.get('DB_VERSION', 'N/A')}")
        insert_sql = getattr(NopQuery, f"INSERT_PRODUCT_SQL_{os.environ.get('DB_VERSION', 'N/A')}")
        product_param_list = [param[col] for col in insert_col_list]
        product = nop_dao.update_r_dict(insert_sql, product_param_list)
        NopData.sku_pid_map[product['Sku']] = product['Id']
        NopData.products_pub_del_tbl[product['Id']] = {'Id': product['Id'],
                                                    'Sku': product['Sku'],
                                                    'Published': product['Published'],
                                                    'Deleted': product['Deleted']}
        return product

    def update_product(product_dict):
        update_col_list = getattr(NopQuery, f"UPDATE_COLUMN_LIST_{os.environ.get('DB_VERSION', 'N/A')}")
        update_sql = getattr(NopQuery, f"UPDATE_PRODUCT_SQL_{os.environ.get('DB_VERSION', 'N/A')}")
        print(update_col_list)
        product_param_list = [product_dict[col] for col in update_col_list]
        nop_dao.update(update_sql, product_param_list)

        return True

    def update_product_status(pid, publish_flag=None, delete_flag=None):
        is_updated_published = False
        is_updated_deleted = False

        product = NopTool.get_product_by_id(pid)
        if publish_flag is not None and product['Published'] != publish_flag:
            product['Published'] = publish_flag
            NopData.products_pub_del_tbl[pid]['Published'] = publish_flag
            is_updated_published = True
        
        if delete_flag is not None and product['Deleted'] != delete_flag:
            product['Deleted'] = delete_flag
            NopData.products_pub_del_tbl[pid]['Deleted'] = delete_flag
            is_updated_deleted = True
        
        if is_updated_published or is_updated_deleted:
            NopTool.update_product(product)
            
        return is_updated_published, publish_flag, is_updated_deleted, delete_flag

    
    def insert_manufacturer(param):
        return nop_dao.update_r_dict(
                NopQuery.INSERT_MANUFACTURER_SQL,
                param
            )
    ##add manufacturer and mappings as needed
    def get_manufacturer(manufacturer_name):
        manufacturer = {}
        if manufacturer_name in NopData.manufacturers.keys():
            manufacturer = NopData.manufacturers[manufacturer_name]

        return manufacturer

    def get_or_create_manufacturer(manufacturer_name):
        manufacturer = {}
        is_created = False
        upper_keys = [key.upper() for key in NopData.manufacturers.keys()]
        if manufacturer_name.upper() not in upper_keys:
            manufacturer = NopTool.insert_manufacturer(
                [manufacturer_name, 
                 "3, 6, 9, 12", 
                 16, True, False, True, False, 
                 0, 0, 0, 0, 1, 0, 10000, 0]
            )
            NopTool.save_slug(manufacturer['Id'], 'Manufacturer', manufacturer['Name'])
            NopData.manufacturers[manufacturer_name] = manufacturer
            is_created = True
        else:
            for key in NopData.manufacturers.keys():
                if key.upper() == manufacturer_name.upper():
                    manufacturer = NopData.manufacturers[key]

        return manufacturer, is_created
            
    def save_product_manufacturer_mapping(pid, manufacturer_id):
        nop_dao.update(NopQuery.DELETE_PRODUCT_MANUFACTURER_MAPPING_SQL, [pid, manufacturer_id])
        return nop_dao.update_r_dict(
            NopQuery.SAVE_PRODUCT_MANUFACTURER_MAPPING_SQL, 
            [pid, manufacturer_id, False, 0]
        )

    def get_slug(param):
        return nop_dao.get_one_row_dict(NopQuery.GET_SLUG_SQL, param)

    def save_slug(entity_id, entity_name, name):
        nop_dao.update(
            NopQuery.DELETE_SLUG_SQL, [entity_id, entity_name]
        )

        slug = slugify(name)

        nop_dao.update(
            NopQuery.INSERT_SLUG_SQL,
            [entity_id, entity_name, slug, True, 0]
        )

        return slug
    
    def update_slug(url_record_id, name):
        slug = slugify(name)

        nop_dao.update(
            NopQuery.UPDATE_SLUG_SQL,
            [slug, url_record_id]
        )

        return slug   

    def save_generic_attribute(entity_id, entity_name, key, value, store_id=0):
        is_updated = False
        prop = nop_dao.get_one_row_dict(
            NopQuery.GET_GENERIC_ATTRIBUTE_SQL, 
            [entity_id, entity_name, key, store_id]
        )
        if prop:
            if prop['Value'].lower().strip() != str(value).lower():
                prop['Value'] = str(value)
                nop_dao.update(
                    NopQuery.UPDATE_GENERIC_ATTRIBUTE_SQL, 
                    [value, prop['Id']]
                )
                is_updated = True
        else:
            prop = nop_dao.update_r_dict(
                NopQuery.INSERT_GENERIC_ATTRIBUTE_SQL, 
                [entity_id, entity_name, key, str(value), store_id]
            )
            is_updated = True

        return prop['Id'], is_updated
       
    def get_generic_attribute(entity_id, entity_name, key, store_id=0):
        prop = nop_dao.get_one_row_dict(
            NopQuery.GET_GENERIC_ATTRIBUTE_SQL, 
            [entity_id, entity_name, key, store_id]
        )
        return prop
        #if prop and prop['Value'].lower().strip() != 'false':
        #    return bool(prop['Value'])
        #else:
        #    return False

    def get_generic_attribute_id_eid_hashmap(key_group, key, store_id=0):
        ga_id_eid_hashmap = nop_dao.get_hashmap(
            NopQuery.GET_GENERIC_ATTRIBUTE_LIST_SQL,
            [key_group, key, store_id])
        return ga_id_eid_hashmap
        
    def delete_generic_attribute(entity_id, entity_name, key):
        nop_dao.update(
            NopQuery.DELETE_GENERIC_ATTRIBUTE_SQL, 
            [entity_id, entity_name, key]
        )
        return True

    def delete_generic_attribute_by_id(ga_id):
        nop_dao.update(
            NopQuery.DELETE_GENERIC_ATTRIBUTE_BY_ID_SQL, 
            [ga_id]
        )
        return True

    def get_product_attribute_by_name(name):
        return nop_dao.get_one_row_dict(
            NopQuery.GET_PRODUCT_ATTRIBUTE_BY_NAME_SQL, name)

    def get_product_attribute_list_by_name(name):
        return nop_dao.get_hashtable(
            NopQuery.GET_PRODUCT_ATTRIBUTE_BY_NAME_SQL, name)

    def insert_product_attribute(param):
        return nop_dao.update_r_dict(
            NopQuery.INSERT_PRODUCT_ATTRIBUTE_SQL, param)

    def delete_product_attribute(param):
        return nop_dao.update(
            NopQuery.DELETE_PRODUCT_ATTRIBUTE_SQL, param)


    def get_predefined_product_attribute_value(product_attribute_id, name=""):
        sql = NopQuery.GET_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_SQL
        if name:
            sql = sql + " AND Name = '" + name + "'"
        return nop_dao.get_one_row_dict(
            sql, [product_attribute_id]
        )
    
    def get_predefined_product_attribute_value_list(product_attribute_id):
        return nop_dao.get_rows_and_keys(
            NopQuery.GET_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_SQL, product_attribute_id
        )

    def insert_predefined_product_attribute_value(param):
        return nop_dao.update_r_dict(
            NopQuery.INSERT_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_SQL, param
        )

    def update_predefined_product_attribute_value(param):
        return nop_dao.update(
            NopQuery.UPDATE_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_PRICE_SQL, param
        )


    def get_product_id_list_by_attribute_id(attr_id):
        return nop_dao.get_one_col_list(
            NopQuery.GET_PRODUCT_ATTRIBUTE_MAPPING_LIST_SQL, attr_id
        )
    
    def get_product_attribute_mapping(product_id, attr_id):
        return nop_dao.get_one_row_dict(
            NopQuery.GET_PRODUCT_ATTRIBUTE_MAPPING_SQL, 
            [product_id, attr_id]
        )
    
    def insert_product_attribute_maping(param):        
        return nop_dao.update_r_dict(
            NopQuery.INSERT_PRODUCT_ATTRIBUTE_MAPPING_SQL, param
        )
    
    def delete_product_attribute_mapping(product_id, attribute_id):
        return nop_dao.update_r_list(
            NopQuery.DELETE_PRODUCT_ATTRIBUTE_MAPPING_SQL, 
            [product_id, attribute_id]
        )

    def delete_product_attribute_mapping_by_paid(attribute_id):
        nop_dao.update(
            NopQuery.DELETE_PRODUCT_ATTRIBUTE_MAPPING_BY_PAID_SQL, 
            attribute_id
        )


    def get_product_attribute_value_list(product_attribute_mapping_id):
        return nop_dao.get_hashtable(
            NopQuery.GET_PRODUCT_ATTRIBUTE_VALUE_SQL, product_attribute_mapping_id
        )

    def get_product_attribute_value(param):
        return nop_dao.get_one_row_dict(
            NopQuery.GET_PRODUCT_ATTRIBUTE_VALUE_BY_NAME_SQL, param
        )

    def update_product_attribute_value(param):
        nop_dao.update(
            NopQuery.UPDATE_PRODUCT_ATTRIBUTE_VALUE_SQL, param
        )

    def delete_product_attribute_value(pam_id):
        nop_dao.update(
            NopQuery.DELETE_PRODUCT_ATTRIBUTE_VALUE_BY_MAPPING_SQL, pam_id
        )

    def insert_product_attribute_value(param):
        nop_dao.update(
            NopQuery.INSERT_PRODUCT_ATTRIBUTE_VALUE_SQL, param
        )

    def get_store_by_name(store_name):
        return nop_dao.get_one_row_dict(
            NopQuery.GET_STORE_BY_NAME_SQL, store_name
        )

    def get_product_store_id_list(pid):
        store_id_list = []

        psm_hashtable = NopTool.get_store_mappings_by_entity_id('Product', pid)
        for psm in psm_hashtable.values():
            if psm['StoreId'] not in store_id_list:
                store_id_list.append(psm['StoreId'])

        return store_id_list

    def save_product_store_mapping(pid, store_id):
        psm = None
        psm = nop_dao.get_one_row_dict(
            NopQuery.GET_STORE_MAPPING_SQL, 
            [pid, 'Product', store_id]
        )
        if not psm:
            psm = nop_dao.update_r_dict(
                NopQuery.INSERT_STORE_MAPPING_SQL, 
                [pid, 'Product', store_id]
            )
            
        return psm

    def save_manufacturer_store_mapping(manufacturer_id, store_id):
        msm = None
        msm = nop_dao.get_one_row_dict(
            NopQuery.GET_STORE_MAPPING_SQL, 
            [manufacturer_id, 'Manufacturer', store_id]
        )
        if not msm:
            msm = nop_dao.update_r_dict(
                NopQuery.INSERT_STORE_MAPPING_SQL, 
                [manufacturer_id, 'Manufacturer', store_id]
            )

        return msm
    

    def save_category_store_mapping(store_id_list, cid):
        for store_id in store_id_list:
            csm = NopTool.get_store_mapping(cid, 'Category', store_id)
            if not csm:
                nop_dao.update(NopQuery.INSERT_STORE_MAPPING_SQL, [cid, 'Category', store_id])

        return True

    def get_store_mappings_by_entity_name(entity_name):
        return nop_dao.get_hashtable(NopQuery.GET_STORE_MAPPINGS_BY_ENTITY_NAME_SQL, [entity_name])
    
    def get_store_mappings_by_entity_id(entity_name, entity_id):
        return nop_dao.get_hashtable(NopQuery.GET_STORE_MAPPINGS_BY_ENTITY_ID_SQL, [entity_name, entity_id])

    def delete_store_mapping_by_id(id):
        nop_dao.update(NopQuery.DELETE_STORE_MAPPING_BY_ID_SQL, [id])

    def delete_store_mapping(store_id, entity_name, entity_id):
        nop_dao.update(NopQuery.DELETE_STORE_MAPPING_SQL, [store_id, entity_name, entity_id])

    def get_store_mapping(entity_id, entity_name, store_id):
        return nop_dao.get_one_row_dict(NopQuery.GET_STORE_MAPPING_SQL, [entity_id, entity_name, store_id])        

    def save_product_category_mapping(pid, cid):
        result = None
        for pcm in NopData.product_category_mappings.values():
            if pcm['ProductId'] == pid and pcm['CategoryId'] == cid:
                result = pcm
                break

        if not result:
            result = nop_dao.update_r_dict(NopQuery.INSERT_PRODUCT_CATEGORY_MAPPING_SQL, [pid, cid, 0, 0])
            pcm_id = result['Id']
            NopData.product_category_mappings[pcm_id] = result            
        
        return result

    def delete_product_category_mapping_by_pid(pid):
        nop_dao.update(NopQuery.DELETE_PRODUCT_CATEGORY_MAPPING_BY_PID_SQL, pid)
        return True

    def delete_product_category_mapping(id):
        nop_dao.update(NopQuery.DELETE_PRODUCT_CATEGORY_MAPPING_SQL, id)
        del NopData.product_category_mappings[id]
        return True
    
    def is_empty_category(category_id):        
        for id, pcm in NopData.product_category_mappings.items():
            if category_id == pcm['CategoryId']:
                product = NopTool.get_product_by_id(pcm['ProductId'])
                if product['Published']:
                    return False                                

        for cid, c in NopData.categories.items():
            if c['ParentCategoryId'] == category_id:
                return NopTool.is_empty_category(cid)

        return True
    
    def get_category_by_name(category_name):
        return nop_dao.get_one_row_dict(NopQuery.GET_CATEGORY_BY_NAME_SQL, category_name)
    
    def get_category_breadcrumb(category):
        breadcrumb_category_id_list = []

        while(category != None and
              (not category['Deleted']) and
              category['Published'] and
              NopTool.get_store_mappings_by_entity_id('Category', category['Id']) and
              (category['Id'] not in breadcrumb_category_id_list) ):            
                
            breadcrumb_category_id_list.append(category['Id'])

            if category['ParentCategoryId']:
                category = NopData.categories[category['ParentCategoryId']]
            else:
                category = None

        if breadcrumb_category_id_list:
            breadcrumb_category_id_list.reverse()

        return breadcrumb_category_id_list
    
    def sort_category_tree(parent_id=0, has_parent_category=False):
        result = []
        sub_category_list = []        

        for category_id, category in NopData.categories.items():
            if (not category['Deleted']) and category['ParentCategoryId'] == parent_id:
                sub_category_list.append(category)

        for category in sub_category_list:
            result.append(category)
            result.extend(NopTool.sort_category_tree(category['Id'], True))

        if (has_parent_category) or (len(result) == len(NopData.categories)):
            return result

        ## If there are some categories in source categories not existing in result 
        ## then it should be added into result finally.
        #for category in NopData.categories.items():
        #    if not next(r for r in result if r['Id'] == category['Id']):
        #        result.append(category)

        return result
    

    # Picture and Product_Picture_Mapping
    def get_picture_by_id(pic_id):
        return nop_dao.get_one_row_dict(NopQuery.GET_PICTURE_BY_ID_SQL, [pic_id])
        
    def get_picture_title_by_pic_id_in_map(pic_id):
        result = None
        if pic_id in NopData.picture_title_map.keys():
            result = NopData.picture_title_map[pic_id]
        return result

    def get_picture_by_title(title_attribute):
        return nop_dao.get_one_row_dict(NopQuery.GET_PICTURE_BY_TITLEATTRIBUTE_SQL, [title_attribute])

    def get_promo_pictures_by_title(store_type, period):
        return nop_dao.get_hashtable(NopQuery.GET_SPECIAL_PROMO_PICTURE_BY_TITLEATTRIBUTE_SQL, ["promo_{}_{}%".format(store_type, period)])

    def get_picture_id_list_by_pid(pid):
        result = []
        for i, ppm in NopData.product_picture_mapping_tbl.items():
            if ppm['ProductId'] == pid:                
                result.append(ppm['PictureId'])
                
        return result   
    
    #def get_product_picture_mapping_tbl_by_pid(pid):
    #    result = {}
    #    for i, ppm in NopData.product_picture_mapping_tbl.items():
    #        if ppm['ProductId'] == pid:
    #            result[i] = ppm
    #    return result
    
    def get_product_picture_mapping_tbl_by_pid(pid):
        result = nop_dao.get_hashtable(NopQuery.GET_PRODUCT_PICTURE_MAPPING_BY_PID_SQL, [pid])
        return result

    def get_product_picture_mapping_id(pid, pic_id):
        ppm_id_list = nop_dao.get_one_col_list(NopQuery.GET_PRODUCT_PICTURE_MAPPING_ID_SQL, [pid, pic_id])
        if not ppm_id_list:
            return None
        # if there is one more duplicated ppm then delete it
        for ppm_id in ppm_id_list[:-1]:
            NopTool.delete_product_picture_mapping_by_id(ppm_id)
        ppm_id = ppm_id_list[0]
        return ppm_id
    
    def get_product_picture_mapping_by_id(ppm_id):
        result = nop_dao.get_one_row_dict(NopQuery.GET_PRODUCT_PICTURE_MAPPING_BY_ID_SQL, [ppm_id])
        return result

    def insert_product_picture_mapping(pid, pic_id, display_order=0):
        ppm = nop_dao.update_r_dict(NopQuery.INSERT_PRODUCT_PICTURE_MAPPING_SQL, [pid, pic_id, display_order])
        NopData.product_picture_mapping_tbl[ppm['Id']]=ppm
        return ppm['Id']

    def update_product_picture_mapping_display_order(id, display_order):        
        nop_dao.update(NopQuery.UPDATE_PRODUCT_PICTURE_MAPPING_DISPLAY_ORDER_SQL, [display_order, id])
        ppm = NopData.product_picture_mapping_tbl[id]
        ppm['DisplayOrder'] = display_order
        return

    def delete_product_picture_mapping(pid, pic_id):
        ppm = nop_dao.update_r_dict(NopQuery.DELETE_PRODUCT_PICTURE_MAPPING_SQL, [pid, pic_id])
        if ppm:
            NopData.product_picture_mapping_tbl.pop(ppm['Id'])
        return

    def delete_product_picture_mapping_by_picid(pic_id):
        nop_dao.update(NopQuery.DELETE_PRODUCT_PICTURE_MAPPING_BY_PICID_SQL, [pic_id])
        return

    def delete_product_picture_mapping_by_pid(pic_id):
        nop_dao.update(NopQuery.DELETE_PRODUCT_PICTURE_MAPPING_BY_PID_SQL, [pic_id])
        return

    def delete_product_picture_mapping_by_id(pmm_id):
        nop_dao.update(NopQuery.DELETE_PRODUCT_PICTURE_MAPPING_BY_ID_SQL, [pmm_id])        
        return

    def update_pic_id_in_product_picture_mapping(old_pic_id, new_pic_id):
        nop_dao.update(NopQuery.UPDATE_PIC_ID_IN_PRODUCT_PICTURE_MAPPING_SQL, [new_pic_id, old_pic_id])
        return

    def insert_picture(mime_type, title_attribute="", seo_filename="", alt_attribute = "", is_new = 1, virtual_path = ""):
        picture = nop_dao.update_r_dict(
            NopQuery.INSERT_PICTURE_SQL, 
            [mime_type, title_attribute, seo_filename, alt_attribute, is_new, virtual_path])
        return picture

    def delete_picture(pic_id):
        nop_dao.update(NopQuery.DELETE_PICTURE_SQL, [pic_id])        
        #nop_dao.update(DELETE_PICTURE_ETAG_SQL, [pic_id])
        NopData.picture_title_map.pop(pic_id, None)
        return

    def get_picture_binary(picture_id):
        return nop_dao.get_one_value(NopQuery.GET_PICTURE_BINARY_SQL, [picture_id])
    
    def get_picture_id_list_by_binary(binary_data):
        return nop_dao.get_one_col_list(NopQuery.GET_PICTURE_ID_BY_BINARY_SQL, [binary_data])

    def update_picture_binary(picture_id, binary):
        nop_dao.update(NopQuery.UPDATE_PICTURE_BINARY_SQL, [binary, picture_id])

    def insert_picture_binary(picture_id, binary):
        result = nop_dao.update_r_dict(NopQuery.INSERT_PICTURE_BINARY_SQL, [picture_id, binary])
        if result:
            return result['Id']        

    def delete_picture_binary(pic_id):
        nop_dao.update(NopQuery.DELETE_PICTURE_BINARY_SQL, [pic_id])

    def get_picture_etag(picture_id):
        etag = nop_dao.get_one_value(NopQuery.GET_PICTURE_ETAG_SQL, [picture_id])
        return etag

    def update_picture_etag(picture_id, etag):
        nop_dao.update(NopQuery.UPDATE_PICTURE_ETAG_SQL, [etag, picture_id])
        return
    
    def insert_picture_etag(picture_id, etag):
        nop_dao.update(NopQuery.INSERT_PICTURE_ETAG_SQL, [picture_id, etag])
        return

    def delete_picture_etag(picture_id):
        nop_dao.update(NopQuery.DELETE_PICTURE_ETAG_SQL, [picture_id])
        return
    
    def get_picture_id_by_etag(etag):
        return nop_dao.get_one_col_list(NopQuery.GET_PICTURE_ID_BY_ETAG, [etag])

    def update_picture_mime_type(picture_id, mime_type):
        nop_dao.update(NopQuery.UPDATE_PICTURE_MIME_TYPE_SQL, [mime_type, picture_id])
        return
    
    def update_picture_title_attribute(picture_id, title_attribute):
        nop_dao.update(NopQuery.UPDATE_PICTURE_TITLE_ATTRIBUTE_SQL, [title_attribute, picture_id])
        return
    
    def update_picture_seo(picture_id, seo_filename):
        nop_dao.update(NopQuery.UPDATE_PICTURE_SEO_SQL, [seo_filename, picture_id])
        return
    

    # SpecificationAttribute
    def save_specification_attribute(name, display_order=0):
        sa_dict = nop_dao.update_r_dict(NopQuery.SAVE_SPECIFICATION_ATTRIBUTE_SQL, [name, display_order])
        return sa_dict
    
    def delete_specification_attribute_by_name_groupid(name, group_id):
        nop_dao.update(NopQuery.DELETE_SPECIFICATION_ATTRIBUTE_BY_NAME_GROUPID_SQL, [name, group_id])

    def delete_specification_attribute_by_name(name):
        nop_dao.update(NopQuery.DELETE_SPECIFICATION_ATTRIBUTE_BY_NAME_SQL, [name])
        
    def save_specification_attribute_option(name, sa_id, display_order):
        sao_dict = nop_dao.update_r_dict(NopQuery.SAVE_SPECIFICATION_ATTRIBUTE_OPTION_SQL, [name, sa_id, display_order])
        return sao_dict
    
    def save_product_specification_attribute_mapping(sao_id, pid):
        psm = nop_dao.update_r_dict(NopQuery.SAVE_PRODUCT_SPECIFICATION_ATTRIBUTE_MAPPING_SQL, [sao_id, pid])
        return psm

    def delete_specification_attribute_options_by_sa_id(sa_id):
        nop_dao.update(NopQuery.DELETE_SPECIFICATION_ATTRIBUTE_OPTIONS_BY_SA_ID_SQL, [sa_id])
    
    
    def save_product_specification_attribute_mapping_v2(pid, attr_type_id, sao_id, allow_filter, show_on_prpage, display_order):
        psm = nop_dao.update_r_dict(NopQuery.SAVE_PRODUCT_SPECIFICATION_ATTRIBUTE_MAPPING_V2_SQL, [pid, attr_type_id, sao_id, allow_filter, show_on_prpage, display_order])
        return psm
    