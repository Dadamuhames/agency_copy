# Generated by Django 5.0 on 2024-06-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_advert_usefullinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='centralapparatus',
            name='subtitle',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regionaladministrations',
            name='subtitle',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
