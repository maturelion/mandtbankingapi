# Generated by Django 3.2.18 on 2023-09-08 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkpoints', '0002_alter_checkpoint_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkpoint',
            name='id',
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
