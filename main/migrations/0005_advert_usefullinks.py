# Generated by Django 5.0 on 2024-06-12 12:25

import custom.models
import easy_thumbnails.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='')),
                ('title', models.JSONField(validators=[custom.models.json_field_validate])),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='')),
                ('title', models.JSONField(validators=[custom.models.json_field_validate])),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
