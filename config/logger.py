import logging.config
import os

logging_config_path = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(logging_config_path)
