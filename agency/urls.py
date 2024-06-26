"""
URL configuration for agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views.static import serve

# import debug_toolbar


urlpatterns = [
    path("admin-panel/", admin.site.urls),
    path("admin/", include("admins.urls")),
    path("api/", include("main.urls")),
    path("api/", include("activities.urls")),
    path("api/", include("education.urls")),
    path("api/", include("service.urls")),
    path("api/", include("regulatory_documents.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="admin/robots.txt", content_type="text/plain"
        ),
    ),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # path("__debug__/", include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
