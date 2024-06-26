from rest_framework import viewsets, generics, filters
from .serializers import *
from .models import *
from custom.views import BasePagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


# DocumentCategory list
class DocumentCategoryList(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentCategory.objects.order_by("order")
    serializer_class = DocumentCategorySerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = DocumentCategoryInnerSerializer
        return super().retrieve(request, *args, **kwargs)


# documents view
class DocumentView(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.select_related("category").order_by("-id")
    serializer_class = DocumentsSerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category__slug"]
    search_fields = ['title']


class OpensourceDocumentsCategoryList(viewsets.ReadOnlyModelViewSet):
    queryset = OpensourceDocumentsCategory.objects.order_by("order")
    serializer_class = OpensourceDocumentsCategorySerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = OpensourceDocumentsCategoryInnerSerializer
        return super().retrieve(request, *args, **kwargs)


class OpensourceDocumentsVIew(viewsets.ReadOnlyModelViewSet):
    queryset = OpensourceDocuments.objects.select_related("category").order_by("-id")
    serializer_class = OpensourceDocumentsSerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category__slug"]
    search_fields = ["title"]
