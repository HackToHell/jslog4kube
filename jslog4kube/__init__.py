# pylint: disable=invalid-name, missing-docstring, too-few-public-methods

import logging
import time
from pythonjsonlogger.jsonlogger import JsonFormatter
from .bootstrap import LOG_ADDS, format_str
from .kube.log_config import LOGGING
from .kube.metadata_injector import KubeMetaInject

JsonFormatter.converter = time.gmtime


try:
    from .gunicorn.dictconfig_logger import GunicornLogger
    HAS_GUNICORN = True
except ImportError:
    HAS_GUNICORN = False


__all__ = ['LOG_ADDS', 'format_str', 'LOGGING']
