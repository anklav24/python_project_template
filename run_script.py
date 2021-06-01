#!/usr/bin/env python3.X
# -*- coding: utf-8 -*-
"""Program entry point."""
import logging
from logging.config import dictConfig

from configs.logging_config import logging_config

dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main():
    pass


if __name__ == '__main__':
    try:
        logger.info("The script was started.")
        main()
        logger.info("The script was ended.")
    except Exception as e:
        logger.exception(e)
