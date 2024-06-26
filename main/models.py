from django.db import models
from custom.models import BaseModel, json_field_validate, ThumbnailerImageField, TimestampModel


# about agency
class AboutAgency(models.Model):
    title = models.JSONField(blank=True, null=True)
    image = ThumbnailerImageField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)    
    short_text = models.JSONField(blank=True, null=True)


# Leadership
class Leadership(BaseModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    subtitle = models.JSONField(blank=True, null=True)
    image = ThumbnailerImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    work_time = models.JSONField(blank=True, null=True)
    short_text = models.JSONField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)


# Central apparatus
class CentralApparatus(BaseModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    subtitle = models.JSONField(blank=True, null=True)
    image = ThumbnailerImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    work_time = models.JSONField(blank=True, null=True)
    short_text = models.JSONField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)


# Regional administrations
class RegionalAdministrations(BaseModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    subtitle = models.JSONField(blank=True, null=True)
    image = ThumbnailerImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    work_time = models.JSONField(blank=True, null=True)
    short_text = models.JSONField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)


# Community council
class CommunityCouncil(BaseModel, TimestampModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    views = models.IntegerField(default=0)


# NewsCategory cateogries
class NewsCategory(BaseModel):
    slug_fields = ['title']

    title = models.JSONField(validators=[json_field_validate])
    text_header = models.JSONField(blank=True, null=True)
    text_footer = models.JSONField(blank=True, null=True)
    order = models.IntegerField(default=0)


# news
class News(BaseModel, TimestampModel):
    slug_fields = ["title"]

    category = models.ForeignKey(NewsCategory, related_name="news", on_delete=models.CASCADE)
    title = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    views = models.IntegerField(default=0)


# banner
class Banner(models.Model):
    image = ThumbnailerImageField(blank=True, null=True)
    title = models.JSONField(validators=[json_field_validate])
    url = models.URLField(blank=True, null=True)


# advert
class Advert(models.Model):
    image = models.JSONField(validators=[json_field_validate])
    title = models.JSONField(validators=[json_field_validate])
    url = models.URLField(blank=True, null=True)


# Useful links
class UsefulLinks(models.Model):
    image = ThumbnailerImageField(blank=True, null=True)
    title = models.JSONField(validators=[json_field_validate])
    url = models.URLField(blank=True, null=True)


# application
class Application(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
