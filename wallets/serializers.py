from rest_framework.serializers import ModelSerializer
from .models import Wallet

class WalletSerializer(ModelSerializer):
    class Meta:
        fields = [
            "url",
            "id",
            "user",
            "balance",
            ]
        model = Wallet
        extra_kwargs = {
            "url": {"view_name": "wallet-detail", "lookup_field": "id"}
        }
