# Generated by Django 3.2.18 on 2024-11-03 11:19

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=users.models.upload_to),
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[['Silver Member', 'Silver Member'], ['Gold Member', 'Gold Member'], ['Platinum Member', 'Platinum Member']], default='Platinum Member', max_length=20),
        ),
    ]
