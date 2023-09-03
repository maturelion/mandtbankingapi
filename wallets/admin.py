from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from wallets.models import Wallet

class WalletAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["user", "balance"]

admin.site.register(Wallet, WalletAdmin)