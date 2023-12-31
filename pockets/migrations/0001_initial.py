# Generated by Django 3.2.18 on 2023-09-04 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=120)),
                ('card_number', models.CharField(max_length=120)),
                ('card_caption', models.CharField(max_length=120)),
                ('card_balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bg_img', models.CharField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
