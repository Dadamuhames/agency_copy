from rest_framework import generics, views, viewsets, response
from .serializers import *
from .models import *
from custom.views import BasePagination
# Create your views here.


# InteractiveServices view
class InteractiveServicesView(generics.ListAPIView):
    queryset = InteractiveServices.objects.order_by("-id")
    serializer_class = InteractiveServicesSerializer
    pagination_class = BasePagination


# SurveyQuestion list
class SurveyQuestionList(generics.ListAPIView):
    queryset = SurveyQuestion.objects.order_by("order").prefetch_related("answers")
    serializer_class = SurveyQuestionSerializer


# answer
class AnswerQuestion(views.APIView):
    def post(self, request, format=None):
        answer_id = request.data.get("answer_id")
        answer = None

        if answer_id is None or not str(answer_id).isnumeric():
            return response.Response({"error": "answer_id invalid"}, status=403)

        try:
            answer = SurveyAnswer.objects.get(id=int(answer_id))
        except:
            return response.Response({"error": "answer_id invalid"}, status=403)
        

        main_survey = MainSurvey(answer=answer)
        main_survey.save()


        return response.Response({"message": "success"}, status=201)


# faq
class FaqList(generics.ListAPIView):
    queryset = Faq.objects.filter(active=True)
    serializer_class = FaqSerializer
    pagination_class = BasePagination


# UserOpinion create
class UserOpinionView(generics.CreateAPIView):
    queryset = UserOpinion.objects.all()
    serializer_class = UserOpinionSerializer


# SecondSurveyServiceList
class SecondSurveyServiceList(generics.ListAPIView): 
    queryset = SecondSurveyService.objects.order_by("order")
    serializer_class = SecondSurveyServiceserializer


# second survey
class SecondSurveyCreate(generics.CreateAPIView):
    queryset = SecondSurvey.objects.all()
    serializer_class = SecondSurveySerializer


# third survey
class ThirdSurveyCreate(generics.CreateAPIView):
    queryset = ThirdSurvey.objects.all()
    serializer_class = ThirdSurveySerializer


# secong survey
class SecondSurveyStatistic(views.APIView):
    def get(self, request, format=None):
        response_data = {}
        servise_id = self.request.GET.get("service_id", 0)

        great_count = SecondSurvey.objects.filter(answer="0")
        good_count = SecondSurvey.objects.filter(answer="1")
        normal_count = SecondSurvey.objects.filter(answer="2")
        bad_count = SecondSurvey.objects.filter(answer="3")

        service = None

        if str(servise_id).isnumeric():
            service = SecondSurveyService.objects.filter(id=int(servise_id)).first()

        if service:
            great_count = great_count.filter(service=service)
            good_count = good_count.filter(service=service)
            normal_count = normal_count.filter(service=service)
            bad_count = bad_count.filter(service=service)

        response_data["great_count"] = great_count.count()
        response_data["good_count"] = good_count.count()
        response_data["normal_count"] = normal_count.count()
        response_data["bad_count"] = bad_count.count()

        return response.Response(response_data)
