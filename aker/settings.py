from pathlib import Path
import environ

# ============================
# Environment Configuration
# ============================
env = environ.Env(
    AKER_ALLOWED_HOSTS=(list, []),
)
env.prefix = "AKER_"

# =======================
# Project Base Directory
# =======================
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================
# Aker Application Settings
# =======================
ADMIN_SITE_TITLE = env("ADMIN_SITE_TITLE")

# ===========================
# Security and Debug Settings
# ===========================
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# =======================
# Installed Applications
# =======================
INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "django_filters",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
    # Project-specific apps
    "core.apps.CoreConfig",
    "policy.apps.PolicyConfig",
    "user.apps.UserConfig",
    "organization.apps.OrganizationConfig",
    "schema.apps.SchemaConfig",
    "field.apps.FieldConfig",
    "record.apps.RecordConfig",
]

# ===================
# Middleware Settings
# ===================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ===================
# URL and WSGI Config
# ===================
ROOT_URLCONF = "aker.urls"
WSGI_APPLICATION = "aker.wsgi.application"

# ====================
# Template Configuration
# ====================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# =======================
# Authentication Settings
# =======================
AUTHENTICATION_BACKENDS = [
    "drf_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]
AUTH_USER_MODEL = "user.User"

# ===========================
# Database Configuration
# ===========================
DATABASES = {
    "default": env.db(),
}

# ============================
# Password Validation Settings
# ============================
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

# ========================
# Internationalization
# ========================
LANGUAGE_CODE = env("LANGUAGE_CODE")
TIME_ZONE = env("TIME_ZONE")
USE_I18N = True
USE_TZ = True

# =======================
# Static Files Settings
# =======================
STATIC_URL = "/static/"
STATIC_ROOT = env("STATIC_ROOT") or BASE_DIR / "staticfiles"

# ======================
# REST Framework Settings
# ======================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "drf_social_oauth2.authentication.SocialAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": env("DEFAULT_PAGE_SIZE"),
    "PAGINATE_BY_PARAM": "page_size",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
    + (
        ["rest_framework.renderers.BrowsableAPIRenderer"]
        if env("ENABLE_BROWSABLE_API")
        else []
    ),
}


# =======================
# Static File Storage
# =======================
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ==============================
# Django Specific Configurations
# ==============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
