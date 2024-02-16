from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@yb+t!s_#0r+&(*xvi1ycpdfc@^_vjv6+j$m@n4d79qt+@s4g5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'complex',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'storages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'elitcity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'elitcity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgresito',
        'USER': 'postgres',
        'PASSWORD': 'postgres5432',
        'HOST': 'database-2.cdrym9kklu4m.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'shikaka12',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {  # This is the root logger
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CORS_ALLOW_ALL_ORIGINS = True






STATICFILES_DIRS = [
    BASE_DIR / 'static'
 ]

MEDIA_ROOT = BASE_DIR / 'static/media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {

        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "static",
        },
    },
}

AWS_ACCESS_KEY_ID = "AKIAVSIQSNG5MQ5K5VNJ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "elitecity"


# Page-pagination using rest
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAdminUserOrReadOnly',
    # ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
SESSION_ENGINE = 'django.contrib.sessions.backends.db'



LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]


MODELTRANSLATION_DEFAULT_LANGUAGE = 'en' 

# IS_MONOLINGUAL=False

USE_I18N = True

MODELTRANSLATION_TRANSLATION_REGISTRY = 'complex.translation'

CSRF_TRUSTED_ORIGINS = ['https://api.storkhome.ge'] 

