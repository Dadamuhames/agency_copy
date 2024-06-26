from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("news/categories", views.NewsCategoryView)
router.register("news", views.NewsView)
router.register("leadership", views.LeadershipView)
router.register("central_apparatus", views.CentralApparatusView)
router.register("regional_administrations", views.RegionalAdministrationsView)
router.register("community_council", views.CommunityCouncilView)


urlpatterns = [
    path("static_infos", views.StaticInfView.as_view()),
    path("translations", views.TranslationsView.as_view()),
    path("languages", views.LangsList.as_view()),
    path("about_agensy", views.AboutAgencyView.as_view()),
    path("banners", views.BannerList.as_view()),
    path("search", views.SearchView.as_view()),
    path("header", views.HeaderAPIView.as_view()),
    path("application/create", views.ApplicationCreate.as_view()),
    path("adverts", views.AdvertList.as_view()),
    path("useful_links", views.UsefulLinksList.as_view())
]

urlpatterns += router.urls
