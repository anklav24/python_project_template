"""Logging configuration file."""
import os
from datetime import datetime

from configs.app_config import logging_level

# replace('\\', '/') for windows capability.
base_dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split("/")[-1]
logs_dir_name = "logs"

if not os.path.exists(logs_dir_name):
    os.makedirs(logs_dir_name)

# Example 2021-05-06T16-08-44_base_dir_name.log
filename = f"{datetime.today().strftime('%Y-%m-%dT%H-%M-%S')}_{base_dir_name}.log"
filepath = os.path.join(logs_dir_name, filename)


logging_config = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'simple_formatter': {
            'format': '%(asctime)s > %(message)s',
        },
        'verbose_formatter': {
            'format': '%(asctime)s > %(levelname)s: %(name)s: %(funcName)s: %(message)s',
        }
    },
    handlers={
        'simple_console_handler': {
            'level': logging_level,
            'formatter': 'simple_formatter',
            'class': 'logging.StreamHandler'
        },
        'console_handler': {
            'level': logging_level,
            'formatter': 'verbose_formatter',
            'class': 'logging.StreamHandler'
        },
        'file_handler': {
            'level': logging_level,
            'formatter': 'verbose_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': filepath,
            'encoding': 'UTF-8',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5
        }
    },
    loggers={
        '': {  # root logger
            'level': logging_level,
            'handlers': ['console_handler', 'file_handler']
        },
        'simple': {
            'level': logging_level,
            'propagate': False,
            'handlers': ['simple_console_handler', 'file_handler']
        },
        '__main__': {
            'level': logging_level,
            'propagate': False,
            'handlers': ['console_handler', 'file_handler']
        }
    },
)
