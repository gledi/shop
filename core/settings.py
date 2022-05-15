import os
from pathlib import Path

import django_heroku
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "zi8-%_#8p^suf+9mjv0ek(7dd#@um9_o)mym9mjh=2whq&@(9="

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "debug_toolbar",
    "django_extensions",
    "fontawesomefree",
    "rest_framework",
    "imagekit",
    "corsheaders",
    # local apps
    "accounts",
    "pages",
    "products",
    "blog",
    "apiv1",
    "apiv2",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

AUTH_USER_MODEL = "accounts.User"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.page_title",
                "core.context_processors.msg_icon",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


sqlite_url = f"sqlite:///{(BASE_DIR / 'db.sqlite3').as_posix()}"
DATABASES = {"default": dj_database_url.parse(os.getenv("DATABASE_URL", sqlite_url))}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ("en-us", "English"),
    ("sq-AL", "Albanian"),
    ("it", "Italian"),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / "assets"]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PAGE_TITLE = "Dyqan Taxi"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework_xml.parsers.XMLParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_xml.renderers.XMLRenderer",
    ],
}

CORS_ALLOW_ALL_ORIGINS = True

DJANGO_HASHIDS_SALT = "o6ur-yzz8x6khr^gjm%cuzlds^otq*0=6xy8jh*6gqki28ty62"
DJANGO_HASHIDS_MIN_LENGTH = 12


if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    SHELL_PLUS_PRINT_SQL = False


django_heroku.settings(locals())
