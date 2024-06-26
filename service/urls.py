from django.urls import path
from . import views

urlpatterns = [
    path("interactive_services", views.InteractiveServicesView.as_view()),
    path("questions", views.SurveyQuestionList.as_view()),
    path("answer", views.AnswerQuestion.as_view()),
    path("faqs", views.FaqList.as_view()),
    path("opinion/save", views.UserOpinionView.as_view()),
    path("services", views.SecondSurveyServiceList.as_view()),
    path("second_survey/answer", views.SecondSurveyCreate.as_view()),
    path("second_survey/statistic", views.SecondSurveyStatistic.as_view()),
    path("third_survey/answer", views.ThirdSurveyCreate.as_view()),
]
