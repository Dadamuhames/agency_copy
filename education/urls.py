from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("education/categories", views.EducationCategoriesList)
router.register("education", views.EducationView)


urlpatterns = [
    path("books", views.BookList.as_view())
]

urlpatterns += router.urls
