from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

ALLOWED_HOSTS = ['3.35.97.110', 'bruteforceuniv.com', 'www.bruteforceuniv.com']
#

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

sentry_sdk.init(
    dsn="https://75abc2620c0e4acdb9f58022930fe088@o1011897.ingest.sentry.io/5976865",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
