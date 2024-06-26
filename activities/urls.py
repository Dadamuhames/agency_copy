from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("activities/categories", views.ActivityCategoriesList)
router.register("activities", views.ActivityView)
router.register("reports", views.ReportView)
router.register("vacansy", views.VacansyView)

urlpatterns = [
    path("investment_potential", views.InvestmentPotentialView.as_view()),
]

urlpatterns += router.urls
