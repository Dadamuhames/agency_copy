from regulatory_documents.models import DocumentCategory, Document
from custom.views import BasedListView, BaseForm


# DocumentCategory list
class DocumentCategoryList(BasedListView):
    model = DocumentCategory
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории документов"
        context["model_name"] = DocumentCategory.__name__
        context["create_url"] = "regulatory_documents_category_create"
        context["edit_url"] = "regulatory_documents_category_edit"
        context["app_name"] = "regulatory_documents"

        return context


# activity category form
class DocumentCategoryForm(BaseForm):
    model = DocumentCategory
    template_name = "admin/category/form.html"
    success_url = "regulatory_documents_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории документов"
        context["model_name"] = DocumentCategory.__name__
        context["list_url"] = "regulatory_documents_category_list"
        context["app_name"] = "regulatory_documents"

        return context


# documents
class DocumentList(BasedListView):
    model = Document
    template_name = "admin/documents/list.html"
    search_fields = ['title']


# documents form
class DocumentsForm(BaseForm):
    model = Document
    template_name = "admin/documents/form.html"
    success_url = "regulatory_documents_list"
    related_model = DocumentCategory
    file_field = "file"
