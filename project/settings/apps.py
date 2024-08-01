# Application definition
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = [
    "admin_auto_filters",
    "admin_interface",
    "colorfield",
    "corsheaders",
    "django_ace",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django_filters",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    "ninja",
    "admin.apps.AdminConfig",
    "access.apps.AccessConfig",
    "pages.apps.PagesConfig",
    "example.apps.ExampleConfig",
]
