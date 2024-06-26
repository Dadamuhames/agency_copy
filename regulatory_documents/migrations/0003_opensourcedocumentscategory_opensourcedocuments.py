# Generated by Django 5.0 on 2024-06-03 12:03

import custom.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_documents', '0002_document_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpensourceDocumentsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('title', models.JSONField(validators=[custom.models.json_field_validate])),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpensourceDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('title', models.JSONField(validators=[custom.models.json_field_validate])),
                ('text', models.JSONField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='regulatory_documents.opensourcedocumentscategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
