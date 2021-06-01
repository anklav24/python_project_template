"""Main application configuration settings."""
import logging
from os import environ

token = environ.get('YOUR_API_TOKEN_NAME')

# Logging
logging_level = "DEBUG"  # "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
exc_info = True  # True, False

# Third-party loggers
logging.getLogger('THIRD_PARTY_LOGGER_NAME').setLevel(logging.WARNING)
