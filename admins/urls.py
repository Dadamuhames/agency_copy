from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

urlpatterns = [
    path("", views.home, name="home"),
    path("langs", views.LangsList.as_view(), name="langs_list"),
    path("langs/create", views.LngCreateView.as_view(), name="create_lang"),
    path("langs/<int:pk>/edit", views.LangsUpdate.as_view(), name="lang_update"),
    path("langs/delete", views.delete_langs, name="lang_del"),
    path("site_infos", views.StaticUpdate.as_view(), name="static_info"),
    path("images/save", views.save_images, name="images_save"),
    path("images/delete", views.delete_image, name="del-img"),
    # translations
    path("translations", views.TranslationList.as_view(), name="translation_list"),
    path(
        "translations/<int:pk>",
        views.TranslationGroupDetail.as_view(),
        name="transl_group_detail",
    ),
    path("translation/edit", views.translation_update, name="translation_edit"),
    path(
        "translations/<int:pk>/edit",
        views.TranslationGroupUdpate.as_view(),
        name="transl_group_edit",
    ),
    path("translations/<int:pk>/delete", views.delete_translation, name="transl_del"),
    path("translation_group/create", views.add_trans_group, name="transl_group_create"),
    path(
        "translations/import", views.translations_from_json, name="translation_import"
    ),
    path("delete", views.delete_item, name="delete"),
    path("lang_icon_delete", views.del_lang_icon, name="lang_icon_del"),
    path("add_static_image", views.add_static_image, name="add_static_logos"),
    path("delete_static_image", views.del_statics_image, name="del_static_image"),
    path(
        "login",
        LoginView.as_view(
            template_name="admin/sing-in.html",
            success_url="/admin/",
        ),
        name="login_admin",
    ),
    path("logout", logout, name="logout_url"),
    path("admins", views.AdminsList.as_view(), name="admin_list"),
    path("admins/create", views.AdminCreate.as_view(), name="admins_create"),
    path("admins/<int:pk>/edit", views.AdminUpdate.as_view(), name="admins_edit"),
    path("delete_model_field", views.delete_model_image, name="delete_model_field"),
    # about agency
    path("about_agency", views.AboutAgencyForm.as_view(), name="about_agency"),
    # leadership
    path("leadership", views.LeadershipList.as_view(), name="leadership_list"),
    path("leadership/create", views.LeadershipForm.as_view(), name="leadership_create"),
    path(
        "leadership/<int:pk>/edit",
        views.LeadershipForm.as_view(),
        name="leadership_edit",
    ),
    # central_apparatus
    path(
        "central_apparatus",
        views.CentralApparatusList.as_view(),
        name="central_apparatus_list",
    ),
    path(
        "central_apparatus/create",
        views.CentralApparatusForm.as_view(),
        name="central_apparatus_create",
    ),
    path(
        "central_apparatus/<int:pk>/edit",
        views.CentralApparatusForm.as_view(),
        name="central_apparatus_edit",
    ),
    # regional_administrations
    path(
        "regional_administrations",
        views.RegionalAdministrationsList.as_view(),
        name="regional_administrations_list",
    ),
    path(
        "regional_administrations/create",
        views.RegionalAdministrationsForm.as_view(),
        name="regional_administrations_create",
    ),
    path(
        "regional_administrations/<int:pk>/edit",
        views.RegionalAdministrationsForm.as_view(),
        name="regional_administrations_edit",
    ),
    # community_council
    path(
        "community_council",
        views.CommunityCouncilList.as_view(),
        name="community_council_list",
    ),
    path(
        "community_council/create",
        views.CommunityCouncilForm.as_view(),
        name="community_council_create",
    ),
    path(
        "community_council/<int:pk>/edit",
        views.CommunityCouncilForm.as_view(),
        name="community_council_edit",
    ),
    path(
        "activity/categories",
        views.ActivityCategoryList.as_view(),
        name="activity_category_list",
    ),
    path(
        "activity/categories/create",
        views.ActivityCategoryForm.as_view(),
        name="activity_category_create",
    ),
    path(
        "activity/categories/<int:pk>/edit",
        views.ActivityCategoryForm.as_view(),
        name="activity_category_edit",
    ),
    path("activity", views.ActivityList.as_view(), name="activity_list"),
    path("activity/create", views.ActivityForm.as_view(), name="activity_create"),
    path("activity/<int:pk>/edit", views.ActivityForm.as_view(), name="activity_edit"),
    path("report", views.ReportsList.as_view(), name="report_list"),
    path("report/create", views.ReportForm.as_view(), name="report_create"),
    path("report/<int:pk>/edit", views.ReportForm.as_view(), name="report_edit"),
    path("vacansy", views.VacansyList.as_view(), name="vacansy_list"),
    path("vacansy/create", views.VacansyForm.as_view(), name="vacansy_create"),
    path("vacansy/<int:pk>/edit", views.VacansyForm.as_view(), name="vacansy_edit"),
    path(
        "investment_potential",
        views.InvestmentPotentialForm.as_view(),
        name="investment_potential_view",
    ),
    path(
        "education/categories",
        views.EducationCategoryList.as_view(),
        name="education_category_list",
    ),
    path(
        "education/categories/create",
        views.EducationCategoryForm.as_view(),
        name="education_category_create",
    ),
    path(
        "education/categories/<int:pk>/edit",
        views.EducationCategoryForm.as_view(),
        name="education_category_edit",
    ),
    path("education", views.EducationList.as_view(), name="education_list"),
    path("education/create", views.EducationForm.as_view(), name="education_create"),
    path(
        "education/<int:pk>/edit", views.EducationForm.as_view(), name="education_edit"
    ),
    path(
        "regulatory_documents/categories",
        views.DocumentCategoryList.as_view(),
        name="regulatory_documents_category_list",
    ),
    path(
        "regulatory_documents/categories/create",
        views.DocumentCategoryForm.as_view(),
        name="regulatory_documents_category_create",
    ),
    path(
        "regulatory_documents/categories/<int:pk>/edit",
        views.DocumentCategoryForm.as_view(),
        name="regulatory_documents_category_edit",
    ),
    path(
        "regulatory_documents",
        views.DocumentList.as_view(),
        name="regulatory_documents_list",
    ),
    path(
        "regulatory_documents/create",
        views.DocumentsForm.as_view(),
        name="regulatory_documents_create",
    ),
    path(
        "regulatory_documents/<int:pk>/edit",
        views.DocumentsForm.as_view(),
        name="regulatory_documents_edit",
    ),
    path(
        "news/categories", views.NewsCategoryList.as_view(), name="news_category_list"
    ),
    path(
        "news/categories/create",
        views.NewsCategoryForm.as_view(),
        name="news_category_create",
    ),
    path(
        "news/categories/<int:pk>/edit",
        views.NewsCategoryForm.as_view(),
        name="news_category_edit",
    ),
    path("news", views.NewsList.as_view(), name="news_list"),
    path("news/create", views.NewsForm.as_view(), name="news_create"),
    path("news/<int:pk>/edit", views.NewsForm.as_view(), name="news_edit"),
    path(
        "documents/categories",
        views.OpensourceDocumentsCategoryList.as_view(),
        name="documents_category_list",
    ),
    path(
        "documents/categories/create",
        views.OpensourceDocumentsCategoriesForm.as_view(),
        name="documents_category_create",
    ),
    path(
        "documents/categories/<int:pk>/edit",
        views.OpensourceDocumentsCategoriesForm.as_view(),
        name="documents_category_edit",
    ),
    path("documents", views.OpensourceDocumentsList.as_view(), name="documents_list"),
    path(
        "documents/create",
        views.OpensourceDocumentsForm.as_view(),
        name="documents_create",
    ),
    path(
        "documents/<int:pk>/edit",
        views.OpensourceDocumentsForm.as_view(),
        name="documents_edit",
    ),
    path("questions", views.QuestionList.as_view(), name="question_list"),
    path("questions/create", views.QuestionForm.as_view(), name="question_create"),
    path("questions/<int:pk>/edit", views.QuestionForm.as_view(), name="question_edit"),
    # faq
    path("faq", views.FaqList.as_view(), name="faq_list"),
    path("faq/create", views.FaqForm.as_view(), name="faq_create"),
    path("faq/<int:pk>/edit", views.FaqForm.as_view(), name="faq_edit"),
    # interactive_service
    path(
        "interactive_service",
        views.InteractiveServiceList.as_view(),
        name="interactive_service_list",
    ),
    path(
        "interactive_service/create",
        views.InteractiveServiceForm.as_view(),
        name="interactive_service_create",
    ),
    path(
        "interactive_service/<int:pk>/edit",
        views.InteractiveServiceForm.as_view(),
        name="interactive_service_edit",
    ),
    # interactive_service
    path("user_opinion", views.UserOpinionList.as_view(), name="user_opinion_list"),
    path(
        "user_opinion/<int:pk>",
        views.UserOpinionDetail.as_view(),
        name="user_opinion_detail",
    ),
    # banner
    path("banners", views.BannerList.as_view(), name="banner_list"),
    path("banners/create", views.BannerForm.as_view(), name="banner_create"),
    path("banners/<int:pk>/edit", views.BannerForm.as_view(), name="banner_edit"),
    # banner
    path("advert", views.AdvertList.as_view(), name="advert_list"),
    path("advert/create", views.AdvertForm.as_view(), name="advert_create"),
    path("advert/<int:pk>/edit", views.AdvertForm.as_view(), name="advert_edit"),
    path("ads/<int:pk>/image/delete", views.delete_ad_image, name="add_image_delete"),
    
    # banner
    path("useful_links", views.UsefulLinksList.as_view(), name="useful_links_list"),
    path(
        "useful_links/create",
        views.UsefulLinksForm.as_view(),
        name="useful_links_create",
    ),
    path(
        "useful_links/<int:pk>/edit",
        views.UsefulLinksForm.as_view(),
        name="useful_links_edit",
    ),
    # banner
    path("service", views.SecondSurveyServiceList.as_view(), name="service_list"),
    path(
        "service/create", views.SecondSurveyServiceForm.as_view(), name="service_create"
    ),
    path(
        "service/<int:pk>/edit",
        views.SecondSurveyServiceForm.as_view(),
        name="service_edit",
    ),
    # banner
    path("books", views.BooksList.as_view(), name="books_list"),
    path("books/create", views.BookForm.as_view(), name="books_create"),
    path("books/<int:pk>/edit", views.BookForm.as_view(), name="books_edit"),
]
