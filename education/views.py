from rest_framework import viewsets, generics, response
from .serializers import EducationCategorySerializer, EducationSerializer, BooksSerializer, EducationDetailSerializer, EducationCategoryInnerSerializer
from .models import *
from custom.views import BasePagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


# categories list
class EducationCategoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = EducationCategory.objects.order_by("order")
    serializer_class = EducationCategorySerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = EducationCategoryInnerSerializer
        return super().retrieve(request, *args, **kwargs)


# education view
class EducationView(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.select_related("category").order_by("-id")
    serializer_class = EducationSerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__slug"]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = EducationDetailSerializer
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


# books view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    pagination_class = BasePagination
