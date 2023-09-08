from django.contrib import admin
from .models import Checkpoint

@admin.register(Checkpoint)
class CheckpointAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "question",
        "answer"
    ]

