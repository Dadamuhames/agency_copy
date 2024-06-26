from custom.serializers import BaseModelSerializer, ThumbnailSerializer
from .models import *
from custom.utils import paginate_related


# education category serializer
class EducationCategorySerializer(BaseModelSerializer):
    class Meta:
        model = EducationCategory
        exclude = ["text_header", "text_footer"]


# education category serializer
class EducationCategoryInnerSerializer(BaseModelSerializer):
    class Meta:
        model = EducationCategory
        fields = "__all__"


# education serializer
class EducationSerializer(BaseModelSerializer):
    category = EducationCategorySerializer()
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Education
        exclude = ['text']

class EducationDetailSerializer(BaseModelSerializer):
    category = EducationCategorySerializer()
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Education
        fields = "__all__"


    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = Education.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = EducationSerializer(
            objects_list, many=True, context={"request": request}
        ).data

        return data


# books serializer
class BooksSerializer(BaseModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
