import sentry_sdk

from .common import *
from sentry_sdk.integrations.django import DjangoIntegration

ALLOWED_HOSTS = ["165.22.118.210"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

sentry_sdk.init(
    dsn="https://751878c9886d41ed853ed05124aa3c62@o516111.ingest.sentry.io/5622155",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {
        "level": "INFO",
        "handlers": ["sentry"],
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "sentry": {
            "level": "INFO",
            "tags": {"custom-tag": "x"},
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "sentry.errors": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
