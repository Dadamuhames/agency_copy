from custom.serializers import BaseModelSerializer, ThumbnailSerializer
from .models import *


# DocumentCategory serializer
class DocumentCategorySerializer(BaseModelSerializer):
    class Meta:
        model = DocumentCategory
        exclude = ['text_header', "text_footer"]


# DocumentCategory serializer
class DocumentCategoryInnerSerializer(BaseModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"


# Document serializer
class DocumentsSerializer(BaseModelSerializer):
    category = DocumentCategorySerializer()

    class Meta:
        model = Document
        fields = '__all__'


# OpensourceDocumentsCategory serializer
class OpensourceDocumentsCategorySerializer(BaseModelSerializer):
    class Meta:
        model = OpensourceDocumentsCategory
        exclude = ["text_header", "text_footer"]


# OpensourceDocumentsCategory serializer
class OpensourceDocumentsCategoryInnerSerializer(BaseModelSerializer):
    class Meta:
        model = OpensourceDocumentsCategory
        fields = '__all__'


# OpensourceDocuments
class OpensourceDocumentsSerializer(BaseModelSerializer):
    category = OpensourceDocumentsCategorySerializer()

    class Meta:
        model = OpensourceDocuments
        fields = "__all__"
