import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = (os.getenv('DEBUG', 'False') == 'True')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'appSignUp.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'appSignUp',
    'appSignIn',
    'appUserManage',
    'appUserManageQuestions',
    'admManageUser',
    'admManageQuestions',
    'utils'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('DB_NAME'),
        'CLIENT': {
            'host': os.getenv('DB_CLIENT')
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ('nickname', 'email',),
        },
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SILENCED_SYSTEM_CHECKS = ['auth.E003', 'auth.W004']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=30),
    "SLIDING_TOKEN_REFRESH_LIFETIME_REMEMBER": timedelta(days=365),
    "SLIDING_TOKEN_LIFETIME_REMEMBER": timedelta(days=730),
    "SLIDING_TOKEN_REFRESH_LIFETIME_LEEWAY": timedelta(minutes=1),
    "SLIDING_TOKEN_LIFETIME_LEEWAY": timedelta(minutes=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "user_id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
    ),
}
