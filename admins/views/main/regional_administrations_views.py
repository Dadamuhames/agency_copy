from custom.views import BasedListView, BaseForm
from main.models import RegionalAdministrations


# RegionalAdministrations list
class RegionalAdministrationsList(BasedListView):
    model = RegionalAdministrations
    template_name = "admin/leadership/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Региональные администрации"
        context["model_name"] = RegionalAdministrations.__name__
        context["create_url"] = "regional_administrations_create"
        context["edit_url"] = "regional_administrations_edit"

        return context


# RegionalAdministrations form
class RegionalAdministrationsForm(BaseForm):
    model = RegionalAdministrations
    template_name = "admin/leadership/form.html"
    success_url = "regional_administrations_list"
    image_field = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Региональные администрации"
        context["model_name"] = RegionalAdministrations.__name__
        context["list_url"] = "regional_administrations_list"

        return context
