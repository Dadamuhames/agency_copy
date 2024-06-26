from custom.utils import NewsVideoSerializer, get_youtube_id, paginate_related
from custom.serializers import BaseModelSerializer, ThumbnailSerializer, JsonFieldSerializer
from rest_framework import serializers
from admins.templatetags.baner_show import baner_thumb
from .models import *


# about agency serializer
class AboutAgencySerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = AboutAgency
        fields = '__all__'


# leadership
class LeadershipListSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Leadership
        exclude = ["text"]


# leadership
class LeadershipSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Leadership
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = Leadership.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = LeadershipListSerializer(objects_list, many=True, context={"request": request}).data

        return data


# CentralApparatus
class CentralApparatusSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = CentralApparatus
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = CentralApparatus.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = CentralApparatusListSerializer(
            objects_list, many=True, context={"request": request}
        ).data

        return data


# CentralApparatus
class CentralApparatusListSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = CentralApparatus
        exclude = ["text"]


# RegionalAdministrations
class RegionalAdministrationsSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = RegionalAdministrations
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = RegionalAdministrations.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = RegionalAdministrationsListSerializer(
            objects_list, many=True, context={"request": request}
        ).data

        return data


# RegionalAdministrations
class RegionalAdministrationsListSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = RegionalAdministrations
        exclude = ["text"]


# CommunityCouncil
class CommunityCouncilSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = CommunityCouncil
        fields = '__all__'

      
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        objects = CommunityCouncil.objects.exclude(id=instance.id)

        objects_list = paginate_related(objects, request)

        data["others"] = CommunityCouncilListSerializer(
            objects_list, many=True, context={"request": request}
        ).data

        return data


# CommunityCouncil
class CommunityCouncilListSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = CommunityCouncil
        exclude = ["text"]


# news category serializer
class NewsCategorySerializer(BaseModelSerializer):
    class Meta:
        model = NewsCategory
        exclude = ["text_header", "text_footer"]


# news category serializer
class NewsCategoryInnerSerializer(BaseModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"


# news serializer
class NewsSerializer(BaseModelSerializer):
    category = NewsCategorySerializer()
    video_url = NewsVideoSerializer()

    class Meta:
        model = News
        exclude = ["text"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["youtube_image"] = None

        video_id = get_youtube_id(instance.video_url)

        if video_id:
            data["youtube_image"] = f"https://img.youtube.com/vi/{video_id}/0.jpg"

        return data


# news detail serializer
class NewsDetailSerializer(NewsSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        news = News.objects.exclude(id=instance.id)

        news_list = paginate_related(news, request)

        data["others"] = NewsSerializer(news_list, many=True, context={"request": request}).data

        return data


# banner serializer
class BannerSerializer(BaseModelSerializer):
    image = ThumbnailSerializer(alias="1100x1100")

    class Meta:
        model = Banner
        fields = '__all__'


# application serializer
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ["created_at"]


# ad serializer
class AdvertSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()

    class Meta:
        model = Advert
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image = JsonFieldSerializer(instance.image, context=self.context).data
        request = self.context.get("request", {})

        data["image"] = baner_thumb(
            image, request=request, alias="1100x1100", return_none=True
        )

        return data


# UsefulLinks
class UsefulLinksSerializer(BaseModelSerializer):
    class Meta:
        model = UsefulLinks
        fields = "__all__"
