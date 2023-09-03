from django.db import models
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def wallet_create(sender, instance=None, created=False, **kwargs):
    if created:
        Wallet.objects.create(user=instance, balance=50.00)

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.user.username