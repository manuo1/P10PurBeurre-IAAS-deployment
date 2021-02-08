import logging
import sentry_sdk

from .common import *
from sentry_sdk.integrations.django import DjangoIntegration

ALLOWED_HOSTS = ["165.22.118.210"]

DEBUG = False

sentry_sdk.init(
    dsn= "https://751878c9886d41ed853ed05124aa3c62@o516111.ingest.sentry.io/5622155",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': [os.path.join(BASE_DIR, 'django.log')]
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

"""
levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
"""
