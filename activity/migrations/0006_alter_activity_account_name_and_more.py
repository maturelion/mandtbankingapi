# Generated by Django 4.2 on 2023-05-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_activity_account_name_activity_account_nunmber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='account_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='account_nunmber',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
