from django.contrib import admin
from .models import Activity
from import_export.admin import ImportExportModelAdmin


class ActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "user",
        "tx_type",
        "amount",
        "status",
        "bank_name",
        "account_name",
        "account_nunmber",
        "routine_nunmber",
        "description",
        "scope",
        "ref",
        "date",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "tx_type",
                    "amount",
                    "status",
                    "bank_name",
                    "account_name",
                    "account_nunmber",
                    "description",
                    "scope",
                    "ref",
                    "date",
                )
            },
        ),
    )


admin.site.register(Activity, ActivityAdmin)
