from django.db import models
from custom.models import json_field_validate, BaseModel, ThumbnailerImageField, TimestampModel
# Create your models here.


# education category
class EducationCategory(BaseModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    text_header = models.JSONField(blank=True, null=True)
    text_footer = models.JSONField(blank=True, null=True)
    order = models.IntegerField(default=0)


# Education
class Education(BaseModel, TimestampModel):
    slug_fields = ["title"]

    category = models.ForeignKey(
        EducationCategory, related_name="educations", on_delete=models.CASCADE
    )
    title = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    views = models.IntegerField(default=0)


# book
class Book(models.Model):
    title = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
