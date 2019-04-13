#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


def configure_logging(log_level=logging.DEBUG):
    """Configure logging."""

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    try:
        sa = logging.StreamHandler(stream=sys.stdout)
    except TypeError:
        sa = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
    sa.setFormatter(formatter)
    logger.addHandler(sa)
    return logger


# Configure logger
logger = configure_logging()
