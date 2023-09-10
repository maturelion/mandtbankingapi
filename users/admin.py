from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin


class UserAdminConfig(ImportExportModelAdmin, UserAdmin):
    model = User
    date_hierarchy = "date_joined"
    search_fields = (
        "email",
        "username",
        "referral"
    )
    list_filter = (
        "is_active",
        "is_staff",
        # "referral",
        "has_miner",
        "can_withdraw_bonus"
    )
    ordering = ("username",)
    list_display = (
        "username",
        # "slug",
        "email",
        "has_miner",
        "referral_code",
        "referral",
        "date_joined",
        "last_login",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "slug",
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                    "has_miner",
                    "can_withdraw_bonus",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            },
        ),
        ("Activity", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
