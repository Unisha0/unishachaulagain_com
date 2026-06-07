from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-in-production-unisha-portfolio-2024'
DEBUG = True
ALLOWED_HOSTS = ['*', 'unishachaulagain.com.np', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', 'English'),
    ('ne', 'नेपाली'),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Contact form email ──
# Messages are always saved to the database (/admin → Contact Messages).
# To also receive them in your inbox, set these and set EMAIL_BACKEND below.
#
# Gmail setup:
#   1. Go to myaccount.google.com → Security → App passwords
#   2. Create an app password for "Mail"
#   3. Paste it as EMAIL_HOST_PASSWORD below
#
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = 'yunishachaulagain001@gmail.com'
EMAIL_HOST_PASSWORD = 'jxmw chcd cnhx rvye'
DEFAULT_FROM_EMAIL  = 'Unisha Portfolio <yunishachaulagain001@gmail.com>'
CONTACT_RECIPIENT_EMAIL = 'yunishachaulagain001@gmail.com'


# ── Summernote rich text editor ──
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '100%',
        'height': '550',
        'lang': 'en-US',
        'toolbar': [
            ['style',    ['style']],
            ['font',     ['bold', 'italic', 'underline', 'strikethrough', 'superscript', 'subscript', 'clear']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color',    ['color']],
            ['para',     ['ul', 'ol', 'paragraph']],
            ['height',   ['height']],
            ['table',    ['table']],
            ['insert',   ['link', 'picture', 'video', 'hr']],
            ['view',     ['fullscreen', 'codeview', 'help']],
        ],
        'fontNames': [
            'Arial', 'Arial Black', 'Comic Sans MS', 'Courier New',
            'Georgia', 'Helvetica', 'Impact', 'Tahoma',
            'Times New Roman', 'Trebuchet MS', 'Verdana',
            'Inter', 'Roboto', 'Open Sans',
        ],
        'fontSizes': ['8','9','10','11','12','14','16','18','20','22','24','28','32','36','48','64'],
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': True,
            'theme': 'monokai',
        },
    },
    'attachment_filesize_limit': 10 * 1024 * 1024,  # 10 MB
    'attachment_upload_to': 'blog/attachments/',
    'disable_attachment': False,
    'attachment_require_authentication': False,
}
