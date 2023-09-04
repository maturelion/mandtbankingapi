from django.db import models
from users.models import User

import environ

env = environ.Env()


def upload_to(instance, filename):
    return f'{env("UPLOAD_LOCATION")}/{instance.user}/{filename}'


class Pocket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=120)
    card_number = models.CharField(max_length=120)
    card_caption = models.CharField(max_length=120)
    card_balance = models.DecimalField(max_digits=12, decimal_places=2)
    bg_img = models.ImageField(blank=True, upload_to=upload_to)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)