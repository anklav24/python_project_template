"""Main application configuration settings."""
import logging
import os

import dotenv

# Utilities
dotenv.load_dotenv(os.path.join('configs', '.env'))

# API
token = os.environ.get('YOUR_API_TOKEN_NAME')

# Logging
logging_level = "DEBUG"  # "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
exc_info = True  # True, False

# Third-party loggers
logging.getLogger('THIRD_PARTY_LOGGER_NAME').setLevel(logging.WARNING)