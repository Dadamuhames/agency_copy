# Generated by Django 5.0 on 2024-06-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadership',
            name='subtitle',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
