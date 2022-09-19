"""
    Settings for the Application.

    Some stuff are may be removed due to not being used.
"""

import os
from pathlib import Path
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

# Environment reader from Docker.
env = Env(
    # Django.
    DEBUG=(bool, False),
    SECRET_KEY=(str, ""),
    ALLOWED_HOSTS=(str, "*"),
    CSRF_TRUSTED_ORIGINS=(str, ["localhost"]),
    # Database.
    POSTGRES_NAME=(str, "django"),
    POSTGRES_USER=(str, "django"),
    POSTGRES_PASSWORD=(str, "postgres"),
    POSTGRES_HOST=(str, "localhost"),
    POSTGRES_PORT=(int, 5432),
    # Application.
    STRIPE_API_PUBLISHABLE_KEY=(str, ""),
    STRIPE_API_SECRET_KEY=(str, ""),
    URL_PREFIX=(str, ""),
)

# Application.
URL_PREFIX = env("URL_PREFIX")
STRIPE_API_PUBLISHABLE_KEY = env("STRIPE_API_PUBLISHABLE_KEY")
STRIPE_API_SECRET_KEY = env("STRIPE_API_SECRET_KEY")

# Django settings.
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(" ")

# Under proxy.
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django modules.
INSTALLED_APPS = [
    "shop.apps.ShopConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database (Docker, PostgreSQL).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_NAME"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Other.
STATIC_ROOT = "static"
ADMIN_MEDIA_PREFIX = "/static/admin"
STATIC_URL = f"/{URL_PREFIX}/static/" if URL_PREFIX else "/static/"
ROOT_URLCONF = "project.urls"
WSGI_APPLICATION = "project.wsgi.application"
