from rest_framework import viewsets, generics, response, views
from .serializers import *
from .models import *
from activities.models import Activity, ActivityCategory
from activities.serializers import ActivitySerializer, ActivityCategorySerializer
from education.models import Education, EducationCategory
from education.serializers import EducationSerializer, EducationCategorySerializer
from regulatory_documents.models import DocumentCategory, OpensourceDocumentsCategory
from regulatory_documents.serializers import DocumentCategorySerializer, OpensourceDocumentsCategorySerializer
from admins.models import *
from custom.views import BasePagination
from .content_serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


# static information
class StaticInfView(views.APIView):
    def get(self, request, format=None):
        obj, _ = StaticInformation.objects.get_or_create(id=1)
        serializer = StaticInformationSerializer(obj, context={"request": request})

        return response.Response(serializer.data)


# translations
class TranslationsView(views.APIView):
    def get(self, request, fromat=None):
        translations = Translations.objects.order_by("-id")
        serializer = TranslationSerializer(translations, context={"request": request})
        return response.Response(serializer.data)


# langs list
class LangsList(generics.ListAPIView):
    queryset = Languages.objects.filter(active=True)
    serializer_class = LangsSerializer
    pagination_class = BasePagination


# AboutAgency
class AboutAgencyView(generics.RetrieveAPIView):
    queryset = AboutAgency.objects.all()
    serializer_class = AboutAgencySerializer

    def get_object(self):
        instance, _ = AboutAgency.objects.get_or_create(id=1)
        return instance


# Leadership view
class LeadershipView(viewsets.ReadOnlyModelViewSet):
    queryset = Leadership.objects.order_by("-id")
    serializer_class = LeadershipListSerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = LeadershipSerializer
        return super().retrieve(request, *args, **kwargs)


# CentralApparatus view
class CentralApparatusView(viewsets.ReadOnlyModelViewSet):
    queryset = CentralApparatus.objects.order_by("-id")
    serializer_class = CentralApparatusListSerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CentralApparatusSerializer
        return super().retrieve(request, *args, **kwargs)


# RegionalAdministrations view
class RegionalAdministrationsView(viewsets.ReadOnlyModelViewSet):
    queryset = RegionalAdministrations.objects.order_by("-id")
    serializer_class = RegionalAdministrationsListSerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = RegionalAdministrationsSerializer
        return super().retrieve(request, *args, **kwargs)


# CommunityCouncil view
class CommunityCouncilView(viewsets.ReadOnlyModelViewSet):
    queryset = CommunityCouncil.objects.order_by("-id")
    serializer_class = CommunityCouncilListSerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CommunityCouncilSerializer
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


# NewsCategory view
class NewsCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = NewsCategory.objects.order_by("order")
    serializer_class = NewsCategorySerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = NewsCategoryInnerSerializer
        return super().retrieve(request, *args, **kwargs)


# News view
class NewsView(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.select_related("category").order_by("-id")
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__slug"]
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = NewsDetailSerializer
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


# banner list
class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = BasePagination


# search
class SearchView(views.APIView):
    def search_leadership(self, search):
        queryset = Leadership.objects.filter(Q(title__icontains=search))[:10]
        return LeadershipListSerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def search_central_apparatus(self, search):
        queryset = CentralApparatus.objects.filter(Q(title__icontains=search))[:10]
        return CentralApparatusListSerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def search_regional_administrations(self, search):
        queryset = RegionalAdministrations.objects.filter(Q(title__icontains=search))[:10]
        return RegionalAdministrationsListSerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def search_community_council(self, search):
        queryset = CommunityCouncil.objects.filter(Q(title__icontains=search))[:10]
        return CommunityCouncilListSerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def search_news(self, search):
        queryset = News.objects.filter(Q(title__icontains=search)).select_related("category")[:10]
        return NewsSerializer(queryset, many=True, context=self.serializer_context).data

    def search_activities(self, search):
        queryset = Activity.objects.filter(Q(title__icontains=search)).select_related(
            "category"
        )[:10]
        return ActivitySerializer(queryset, many=True, context=self.serializer_context).data

    def search_educations(self, search):
        queryset = Education.objects.filter(Q(title__icontains=search)).select_related(
            "category"
        )[:10]
        return EducationSerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def get(self, request, format=None):
        self.serializer_context = {"request": request}
        search = self.request.GET.get("search")

        result = {}

        result['leaderships'] = self.search_leadership(search)
        result["central_apparatus"] = self.search_central_apparatus(search)
        result["regional_administrations"] = self.search_regional_administrations(search)
        result["community_council"] = self.search_community_council(search)
        result["news"] = self.search_news(search)
        result["activities"] = self.search_activities(search)
        result["educations"] = self.search_educations(search)

        return response.Response(result)


# header API
class HeaderAPIView(views.APIView):
    def get_news_categories(self):
        queryset = NewsCategory.objects.order_by("order")[:20]
        return NewsCategorySerializer(queryset, many=True, context=self.serializer_context).data

    def get_activities_categories(self):
        queryset = ActivityCategory.objects.order_by("order")[:20]
        return ActivityCategorySerializer(queryset, many=True, context=self.serializer_context).data

    def get_educations_categories(self):
        queryset = EducationCategory.objects.order_by("order")[:20]
        return EducationCategorySerializer(queryset, many=True, context=self.serializer_context).data

    def get_document_categories(self):
        queryset = DocumentCategory.objects.order_by("order")[:20]
        return DocumentCategorySerializer(queryset, many=True, context=self.serializer_context).data

    def get_open_source_categories(self):
        queryset = OpensourceDocumentsCategory.objects.order_by("order")[:20]
        return OpensourceDocumentsCategorySerializer(
            queryset, many=True, context=self.serializer_context
        ).data

    def get(self, request, format=None):
        self.serializer_context = {"request": request}

        result = {}

        result["news_categories"] = self.get_news_categories()
        result["activity_categories"] = self.get_activities_categories()
        result["education_categories"] = self.get_educations_categories()
        result["document_categories"] = self.get_document_categories()
        result["open_source_categories"] = self.get_open_source_categories()

        return response.Response(result)


# application create
class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


# advert list
class AdvertList(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


# UsefulLinks list
class UsefulLinksList(generics.ListAPIView):
    queryset = UsefulLinks.objects.all()
    serializer_class = UsefulLinksSerializer
    pagination_class = BasePagination
