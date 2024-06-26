from rest_framework import serializers
from admins.models import StaticInformation, MetaTags
from custom.serializers import *


# meta serializer
class MetaFieldSerializer(BaseModelSerializer):
    class Meta:
        model = MetaTags
        exclude = ['id']


# static information
class StaticInformationSerializer(BaseModelSerializer):
    logo_first = ThumbnailSerializer(alias='prod_photo')
    logo_second = ThumbnailSerializer(alias='prod_photo')

    class Meta:
        model = StaticInformation
        exclude = ['id']


# translation serializer
class TranslationSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = {}

        for item in instance:
            val = JsonFieldSerializer(
                item.value, context={'request': self.context.get('request')}).data
            key = str(item.group.sub_text) + '.' + str(item.key)
            data[key] = val

        return data


# langs serializer
class LangsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'
        