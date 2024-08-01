import os
from django.conf import settings
from django.urls import path, include

from api.routes import router

os.environ["NINJA_SKIP_REGISTRY"] = "yes"


urlpatterns = [
    path("api/", router.urls),
    path("auth/", include("allauth.urls")),
    path("", include("pages.urls")),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(path(settings.ADMIN_URL_PATH, include("admin.urls")))

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
