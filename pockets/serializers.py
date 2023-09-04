from rest_framework.serializers import ModelSerializer
from .models import Pocket


class PocketSerializer(ModelSerializer):
    class Meta:
        fields = [
            "url",
            "id",
            "user",
            "card_name",
            "card_number",
            "card_caption",
            "card_balance",
            "bg_img",
        ]
        model = Pocket
        extra_kwargs = {
            "url": {"view_name": "pocket-detail", "lookup_field": "id"}
        }
