from .common import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (
                '%(asctime)s [%(process)d] [%(levelname)s] '
                + 'pathname=%(pathname)s lineno=%(lineno)s '
                + 'funcname=%(funcName)s %(message)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {'format': '%(levelname)s %(message)s'},
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
}

DEBUG_PROPAGATE_EXCEPTIONS = True
