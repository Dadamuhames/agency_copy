from custom.views import BasedListView, BaseForm
from main.models import CentralApparatus


# CentralApparatus list
class CentralApparatusList(BasedListView):
    model = CentralApparatus
    template_name = "admin/leadership/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Центральный аппарат"
        context["model_name"] = CentralApparatus.__name__
        context["create_url"] = "central_apparatus_create"
        context["edit_url"] = "central_apparatus_edit"

        return context


# CentralApparatus form
class CentralApparatusForm(BaseForm):
    model = CentralApparatus
    template_name = "admin/leadership/form.html"
    success_url = "central_apparatus_list"
    image_field = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Центральный аппарат"
        context["model_name"] = CentralApparatus.__name__
        context["list_url"] = "central_apparatus_list"

        return context
