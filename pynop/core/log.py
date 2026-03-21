import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import os
import pickle
import settings

BIG_DIVIDER = """
======================================================================
"""

DIVIDER = """
----------------------------------------------------------------------
"""

BIG_LINEFEED = "\n\n"
LINEFEED = "\n"


class DataLogger:
	def __init__(self, biz_name='DataBiz', log_level='INFO', log_dir_path='./', app_started_time=datetime.now()):
		
		if not os.path.exists(log_dir_path):
			os.makedirs(log_dir_path)

		self.log_level = log_level.upper()
		self.log_dir_path = log_dir_path
		self.app_started_time = app_started_time

		logging.basicConfig(
			#level=logging.DEBUG,
		    #format="%(asctime)s [%(biz_name)-2s] %(levelname)-2s: %(message)s",
		)
		
		self.logger = logging.getLogger(biz_name)
		
		if self.log_level == 'DEBUG':
			self.logger.setLevel(logging.DEBUG)
		elif self.log_level == 'INFO':
			self.logger.setLevel(logging.INFO)
		elif self.log_level == 'WARNING':
			self.logger.setLevel(logging.WARNING)
		elif self.log_level == 'ERROR':
			self.logger.setLevel(logging.ERROR)
		elif self.log_level == 'FATAL' or log_level == 'CRITICAL':
			self.logger.setLevel(logging.CRITICAL)
		else:
			raise ValueError('unknown logging level')

		log_filename = self.app_started_time.strftime("%Y%m%d_%H%M%S") + "_" + biz_name + ".log"
		self.log_filename = os.path.join(self.log_dir_path, log_filename)

		trh = TimedRotatingFileHandler(self.log_filename, when='D', interval=1, backupCount=settings.LOG_MAX_RETENTION_DAYS, encoding="utf8")
		trh.suffix = "%Y%m%d_%H%M%S"
		self.logger.addHandler(trh)
		
		ABC_SIGNATURE = f"""
======================================================================
	*Task Title : ABC Sync -> {biz_name}
	*Started Time : {app_started_time}
======================================================================
"""
		self.log(ABC_SIGNATURE, log_level)

	def end(self):
		handlers = self.logger.handlers[:]
		for handler in handlers:
			handler.close()
			self.logger.removeHandler(handler)

	def log(self, msg, log_level="warning"):		
		if log_level.lower() == "warning":
			self.logger.warning(msg)
		elif log_level.lower() == "info":
			self.logger.info(msg)
		elif log_level.lower() == "debug":
			self.logger.debug(msg)
		elif log_level.lower() == "error":
			self.logger.error(msg)

	def log_big_divider(self, log_level="warning"):
		self.log(BIG_DIVIDER, log_level)

	def log_divider(self, log_level="warning"):
		self.log(DIVIDER, log_level)

	def log_big_linefeed(self, log_level="warning"):
		self.log(BIG_LINEFEED, log_level)
				
	def log_linefeed(self, log_level="warning"):
		self.log(LINEFEED, log_level)

	def log_task_title(self, title="", log_level="warning"):
		if not title:
			title = self.logger.name
		TITLE_SPACES = "	  "
		msg = BIG_DIVIDER + LINEFEED + TITLE_SPACES + title + DIVIDER + LINEFEED
		self.log(msg, log_level)

	def log_func_title(self, title="", log_level="info"):		
		msg = LINEFEED + LINEFEED + "- " + title + DIVIDER
		self.log(msg, log_level)

	def log_current_time(self):
		self.log(LINEFEED + "** Started Time : {s}".format(s = self.app_started_time))
		self.log(LINEFEED + "** Current Time : {c}".format(c = datetime.now()))
		self.log(LINEFEED + "**  Wasted Time : {w}".format(w = datetime.now() - self.app_started_time))

	def log_step(self, step="", log_level="info"):
		msg = LINEFEED + BIG_DIVIDER + LINEFEED + ".. " + step + LINEFEED
		self.log(msg, log_level)

	def log_data(self, data={}, log_level="debug"):
		for k, v in data.items():			
			self.log(f"{k} : {v}", log_level)

	def log_biz_msg(self, msg_title, msg_text, log_level="info"):
		msg = LINEFEED + "*" + msg_title + ":" + LINEFEED + "  " + msg_text
		self.log(msg, log_level)

	def log_query(self, sql_name, sql):
		self.log_divider("debug")
		self.log_biz_msg(sql_name + "=\n", sql, "debug")

	def log_query_result(self, sql_name, result):
		self.log_biz_msg(sql_name + "_RESULT", str(result) + " rows", "debug")
		self.log_divider("debug")

	def dump_data(self, filename, data):
		with open(filename, 'wb') as filehandle:
			pickle.dump(data, filehandle, protocol=pickle.HIGHEST_PROTOCOL)

	def load_data(self, filename):
		with open(filename, 'rb') as filehandle:
			return pickle.load(filehandle)

	def cleanup_expired_log(self, log_dir, max_retention_days):
		today = datetime.now()
		for filename in os.listdir(log_dir):
			file_path = os.path.join(log_dir, filename)
			if os.path.isfile(file_path):
				file_creation_time = datetime.fromtimestamp(os.path.getmtime(file_path))
				if (today - file_creation_time).days > max_retention_days:
					os.remove(file_path)

