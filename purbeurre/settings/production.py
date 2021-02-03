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

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
