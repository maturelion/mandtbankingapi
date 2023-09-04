from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Pocket


class PocketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["user",
                    "card_name",
                    "card_number",
                    "card_caption",
                    "card_balance",
                    "bg_img"
                    ]


admin.site.register(Pocket, PocketAdmin)
