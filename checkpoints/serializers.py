from rest_framework.serializers import ModelSerializer
from .models import Checkpoint

class CheckpointSerializers(ModelSerializer):
    class Meta:
        fields = [
            "user",
            "question",
            "answer"
        ]
        model = Checkpoint
        extra_kwargs = {
            "url": {"view_name": "checkpoint-detail", "lookup_field": "user_id"}
        }
