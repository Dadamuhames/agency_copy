# Generated by Django 5.0 on 2024-06-10 12:08

import custom.models
import easy_thumbnails.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='')),
                ('title', models.JSONField(validators=[custom.models.json_field_validate])),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
