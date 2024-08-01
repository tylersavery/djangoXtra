from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from admin.models import ModelAdmin
from .models import Color


@admin.register(Color)
class ColorAdmin(ModelAdmin):
    search_fields = ["name", "color"]
    autocomplete_fields = ["owner"]
    readonly_fields = [
        "uuid",
        "created_at",
        "updated_at",
    ]

    list_display = [
        "hex",
        "name",
        "owner",
        "created_at",
    ]

    list_filter = [
        AutocompleteFilterFactory(_("Owner"), "owner"),
    ]

    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "uuid",
                    "hex",
                    "name",
                    "owner",
                ]
            },
        ),
        (
            _("Dates"),
            {
                "fields": [
                    "created_at",
                    "updated_at",
                ]
            },
        ),
        (
            _("Data"),
            {
                "fields": [
                    "metadata",
                ]
            },
        ),
    )

    class Media:
        pass
