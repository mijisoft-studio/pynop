import functools
import traceback
from datetime import datetime

from .log import DataLogger

import settings
from .exceptions import BizError


def timestamp():
    """Return current timestamp as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def mark(func):
    """Decorator to print markers with timestamps before, after, and on exceptions."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # assume first arg is self
        self = args[0]
        logger = getattr(self, "logger", None)

        start_msg = f"[{timestamp()}] --- START {func.__qualname__} ---"
        end_msg = f"[{timestamp()}] --- END {func.__qualname__} ---"

        try:
            if logger:
                logger.info(start_msg)
            else:
                print(start_msg)

            result = func(*args, **kwargs)

            if logger:
                logger.info(end_msg)
            else:
                print(end_msg)

            return result
        except Exception as e:
            err_msg = f"[{timestamp()}] !!! ERROR in {func.__qualname__}: {e}"
            if logger:
                logger.error(err_msg)
            else:
                print(err_msg)
            traceback.print_exc()
            raise

        return wrapper


def auto_mark_methods(cls):
    """Class decorator to apply `mark` to all methods of a class."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, mark(attr_value))
    return cls


class Biz:
    """
    Abstract class to describe business logic of sync program.
    """

    def __init__(self, settings):
        log_level = settings.LOG_LEVEL_OPTION
        log_dir_path = settings.LOG_DIR_PATH
        app_started_time = settings.APP_STARTED_TIME
        self.logger = DataLogger(str(type(self).__name__), log_level, log_dir_path, app_started_time)

        self.reports = {}

    def start_biz(self):
        pass

    def end_biz(self):
        self.logger.log_divider()
        self.logger.log_biz_msg("Biz Reports", str(self.reports))
        self.logger.log_current_time()
        self.logger.log_divider()
        self.logger.cleanup_expired_log(settings.LOG_DIR_PATH, settings.LOG_MAX_RETENTION_DAYS)
        self.logger.end()

    def run(self):
        try:
            self.start_biz()
            self.end_biz()
        except Exception as e:
            self.logger.log_biz_msg("Biz Error", str(e))
            raise e
        finally:
            pass

