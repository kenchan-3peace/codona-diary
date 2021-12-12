from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#ALLOWED_HOSTS = ['codona-diary.herokuapp.com']
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggiers': False,

    # ロガーの設定
    'loggers': {
        # djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    #ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },
    #フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
