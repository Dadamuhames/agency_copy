from regulatory_documents.models import OpensourceDocuments, OpensourceDocumentsCategory
from custom.views import BasedListView, BaseForm


# open source categories list
class OpensourceDocumentsCategoryList(BasedListView):
    model = OpensourceDocumentsCategory
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории документов"
        context["model_name"] = OpensourceDocumentsCategory.__name__
        context["create_url"] = "documents_category_create"
        context["edit_url"] = "documents_category_edit"
        context["app_name"] = "regulatory_documents"

        return context


# open source documents categories form
class OpensourceDocumentsCategoriesForm(BaseForm):
    model = OpensourceDocumentsCategory
    template_name = "admin/category/form.html"
    success_url = "documents_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории документов"
        context["model_name"] = OpensourceDocumentsCategory.__name__
        context["list_url"] = "documents_category_list"
        context["app_name"] = "regulatory_documents"

        return context


# open source documents
class OpensourceDocumentsList(BasedListView):
    model = OpensourceDocuments
    template_name = "admin/report/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Открытые данные"
        context["model_name"] = OpensourceDocuments.__name__
        context["create_url"] = "documents_create"
        context["edit_url"] = "documents_edit"
        context["app_name"] = "regulatory_documents"

        return context


# open source documents
class OpensourceDocumentsForm(BaseForm):
    model = OpensourceDocuments
    template_name = "admin/report/form.html"
    success_url = "documents_list"
    file_field = "file"
    exclude_fields = ["created_at", "updated_at"]
    related_model = OpensourceDocumentsCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Открытые данные"
        context["model_name"] = OpensourceDocuments.__name__
        context["list_url"] = "documents_list"
        context["app_name"] = "regulatory_documents"

        return context
