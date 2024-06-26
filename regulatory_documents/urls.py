from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(
    "opensourse_documents/categories", views.OpensourceDocumentsCategoryList
)
router.register("documents/categories", views.DocumentCategoryList)
router.register("documents", views.DocumentView)
router.register("opensourse_documents", views.OpensourceDocumentsVIew)


urlpatterns = []
urlpatterns += router.urls
