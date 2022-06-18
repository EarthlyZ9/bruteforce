from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
ALLOWED_HOSTS = [".ap-northeast-2.compute.amazonaws.com",
                 ".bruteforceuniv.com",
                 'www.bruteforceuniv.com',
                 '.ap-northeast-2.elb.amazonaws.com']

STATIC_ROOT = os.path.join(BASE_DIR, '/static')
STATICFILES_DIRS = []

sentry_sdk.init(
    dsn="https://665ae8be2eb24878bd15aa64ab84cd6f@o1011897.ingest.sentry.io/6508324",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
