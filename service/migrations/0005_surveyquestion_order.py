# Generated by Django 5.0 on 2024-06-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_useropinion_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
