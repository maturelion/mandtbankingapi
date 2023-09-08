from django.db import models
from users.models import User


class Checkpoint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)
