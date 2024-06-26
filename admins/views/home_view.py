from django.shortcuts import render
from service.models import MainSurvey, SecondSurvey, ThirdSurvey, SurveyAnswer, SurveyQuestion
from django.db.models import Prefetch, Count

# home admin
def home(request):
    context = {}

    questions = SurveyQuestion.objects.prefetch_related(Prefetch("answers", SurveyAnswer.objects.annotate(selected__count=Count("selecteds")).order_by("order")))    

    context["questions"] = questions

    rate_answers = []

    rate_answers.append(ThirdSurvey.objects.filter(answer="0").count())
    rate_answers.append(ThirdSurvey.objects.filter(answer="1").count())
    rate_answers.append(ThirdSurvey.objects.filter(answer="2").count())
    rate_answers.append(ThirdSurvey.objects.filter(answer="3").count())

    context["rate_answers"] = rate_answers

    return render(request, 'admin/dashboard.html', context=context)
