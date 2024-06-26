from custom.serializers import BaseModelSerializer, ThumbnailSerializer
from custom.utils import paginate_related
from .models import *

# activity categories serializers
class ActivityCategorySerializer(BaseModelSerializer):
    class Meta:
        model = ActivityCategory
        exclude = ["text_header", "text_footer"]


# activity categories serializers
class ActivityCategoryInnerSerializer(BaseModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'


# activity serializer
class ActivitySerializer(BaseModelSerializer):
    category = ActivityCategorySerializer()
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Activity
        exclude = ['text']


# activity serializer
class ActivityDetailSerializer(BaseModelSerializer):
    category = ActivityCategorySerializer()
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Activity
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = Activity.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = ActivitySerializer(
            objects_list, many=True, context={"request": request}
        ).data

        return data


# report serializer
class ReportSerializer(BaseModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


# vacansy serializer
class VacansySerializer(BaseModelSerializer):
    class Meta:
        model = Vacansy
        fields = '__all__'


# InvestmentPotential
class InvestmentPotentialSerializers(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")
    
    class Meta:
        model = InvestmentPotential
        fields = '__all__'
