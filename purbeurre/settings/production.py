import sentry_sdk

from .common import *
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

ALLOWED_HOSTS = ["165.22.118.210"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.INFO  # Send errors as events
)

sentry_sdk.init(
    dsn="https://751878c9886d41ed853ed05124aa3c62@o516111.ingest.sentry.io/5622155",
    integrations=[DjangoIntegration(), sentry_logging],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)
