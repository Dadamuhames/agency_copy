# Generated by Django 5.0 on 2024-06-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_alter_investmentpotential_title_alter_vacansy_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentpotential',
            name='short_text',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
