from rest_framework import serializers
from custom.serializers import BaseModelSerializer, ThumbnailSerializer
from .models import *


# InteractiveServices serializer
class InteractiveServicesSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = InteractiveServices
        fields = '__all__'


# survey answer serializer
class SurveyAnswerSerializer(BaseModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = ["id", "answer", "order"]


# survey question serializer
class SurveyQuestionSerializer(BaseModelSerializer):
    answers = SurveyAnswerSerializer(many=True)

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


# faq serializer
class FaqSerializer(BaseModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


# UserOpinion
class UserOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOpinion
        fields = '__all__'


# SecondSurveyService
class SecondSurveyServiceserializer(BaseModelSerializer):
    class Meta:
        model = SecondSurveyService
        fields = '__all__'


# SecondSurvey serializer
class SecondSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSurvey
        fields = '__all__'


# third survey
class ThirdSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdSurvey
        fields = '__all__'