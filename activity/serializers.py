from rest_framework.serializers import ModelSerializer

from .models import Activity

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
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
            "date"
        ]