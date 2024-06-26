from rest_framework import generics, viewsets, response
from .serializers import *
from .models import *
from custom.views import BasePagination
from django_filters.rest_framework import DjangoFilterBackend

# activity category
class ActivityCategoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityCategory.objects.order_by("order")
    serializer_class = ActivityCategorySerializer
    pagination_class = BasePagination
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ActivityCategoryInnerSerializer
        return super().retrieve(request, *args, **kwargs)


# activity
class ActivityView(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.select_related("category").order_by("-id")
    serializer_class = ActivitySerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__slug"]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ActivityDetailSerializer
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


# report view
class ReportView(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.order_by("-id")
    serializer_class = ReportSerializer
    pagination_class = BasePagination


# Vacansy view
class VacansyView(viewsets.ReadOnlyModelViewSet):
    queryset = Vacansy.objects.order_by("-id")
    serializer_class = VacansySerializer
    pagination_class = BasePagination


# InvestmentPotential
class InvestmentPotentialView(generics.RetrieveAPIView):
    queryset = InvestmentPotential.objects.all()
    serializer_class = InvestmentPotentialSerializers

    def get_object(self):
        instance, _ = InvestmentPotential.objects.get_or_create(id=1)
        return instance
