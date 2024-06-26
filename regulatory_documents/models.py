from django.db import models
from custom.models import json_field_validate, BaseModel, TimestampModel
# Create your models here.


# document cateogries
class DocumentCategory(BaseModel):  
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    text_header = models.JSONField(blank=True, null=True)
    text_footer = models.JSONField(blank=True, null=True)
    order = models.IntegerField(default=0)


# documents
class Document(models.Model):
    category = models.ForeignKey(
        DocumentCategory, related_name="documents", on_delete=models.CASCADE
    )
    title = models.JSONField(validators=[json_field_validate])
    code = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    text = models.JSONField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)


# opensource documents category
class OpensourceDocumentsCategory(BaseModel):
    slug_fields = ["title"]

    title = models.JSONField(validators=[json_field_validate])
    text_header = models.JSONField(blank=True, null=True)
    text_footer = models.JSONField(blank=True, null=True)
    order = models.IntegerField(default=0)


# OpensourceDocuments
class OpensourceDocuments(BaseModel, TimestampModel):
    category = models.ForeignKey(
        OpensourceDocumentsCategory, related_name="documents", on_delete=models.CASCADE
    )
    title = models.JSONField(validators=[json_field_validate])
    text = models.JSONField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
