from django.urls import path, include

from .views import ColorsPageView, ColorPageView

app_name = "example"

urlpatterns = [
    path("colors/", ColorsPageView.as_view(), name="colors"),
    path("colors/<uuid:uuid>/", ColorPageView.as_view(), name="color"),
]
