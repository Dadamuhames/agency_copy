from django.db import models
from custom.models import (
    BaseModel,
    json_field_validate,
    ThumbnailerImageField,
    TimestampModel,
)

# Create your models here.


# Activity category
class ActivityCategory(BaseModel):
    slug_fields = ['title']

    title = models.JSONField(validators=[json_field_validate])
    text_header = models.JSONField(blank=True, null=True)
    text_footer = models.JSONField(blank=True, null=True)
    order = models.IntegerField(default=0)

# article
class Activity(BaseModel, TimestampModel):
    slug_fields = ['title']

    category = models.ForeignKey(
        ActivityCategory, related_name="activities", on_delete=models.CASCADE
    )
    title = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    views = models.IntegerField(default=0)


# Reports
class Report(TimestampModel):
    title = models.JSONField(validators=[json_field_validate])
    text = models.JSONField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)


# vacansy
class Vacansy(TimestampModel):
    title = models.JSONField(validators=[json_field_validate])
    text = models.JSONField(blank=True, null=True)
    views = models.IntegerField(default=0)
    date = models.DateField()


# Investment potential
class InvestmentPotential(TimestampModel):
    title = models.JSONField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    short_text = models.JSONField(blank=True, null=True)
    image = ThumbnailerImageField(blank=True, null=True)
