from django.db import models
from custom.models import json_field_validate, ThumbnailerImageField
# Create your models here.


# interactive services
class InteractiveServices(models.Model):
    title = models.JSONField(validators=[json_field_validate])
    url = models.JSONField(validators=[json_field_validate])
    image = ThumbnailerImageField(blank=True, null=True)


# survey questions
class SurveyQuestion(models.Model):
    question = models.JSONField(validators=[json_field_validate])
    order = models.IntegerField(default=0)


# survey answers
class SurveyAnswer(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name="answers")
    answer = models.JSONField(validators=[json_field_validate])
    order = models.IntegerField()


# main survey
class MainSurvey(models.Model):
    answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE, related_name="selecteds")
    created_at = models.DateTimeField(auto_now_add=True)


# faq
class Faq(models.Model):
    question = models.JSONField(validators=[json_field_validate])
    answer = models.JSONField(validators=[json_field_validate])
    active = models.BooleanField(default=True)


# user opinion
class UserOpinion(models.Model):
    TYPES = (("opinion", "Fikr va takliflar"), 
             ("appeal", "Jismoniy va yuridik shaxslarning murjaatlari"))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    topic = models.CharField(max_length=255)
    text = models.TextField()
    type = models.CharField(max_length=255, choices=TYPES)
    created_at = models.DateTimeField(auto_now_add=True)


# survey service
class SecondSurveyService(models.Model):
    title = models.JSONField(validators=[json_field_validate])
    order = models.IntegerField(default=0)

# second survey
class SecondSurvey(models.Model):
    ANSWERS = (
        ("0", "A’lo darajada"),
        ("1", "Yaxshi darajada"),
        ("2", "Qoniqarli darajada"),
        ("3", "Qoniqarsiz darajada"),
    )

    service = models.ForeignKey(SecondSurveyService, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, choices=ANSWERS)


# third survey
class ThirdSurvey(models.Model):
    ANSWERS = (
        ("0", "Variant 0"),
        ("1", "Variant 1"),
        ("2", "Variant 2"),
        ("3", "Variant 3"),
    )

    answer = models.CharField(max_length=255, choices=ANSWERS)
