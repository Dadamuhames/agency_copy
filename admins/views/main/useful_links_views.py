from main.models import UsefulLinks
from custom.views import BasedListView, BaseForm


# UsefulLinks list
class UsefulLinksList(BasedListView):
    model = UsefulLinks
    template_name = "admin/banner/list.html"
    search_fields = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Полезные ссылки"
        context["model_name"] = UsefulLinks.__name__
        context["create_url"] = "useful_links_create"
        context["edit_url"] = "useful_links_edit"
        context["app_name"] = "main"

        return context


# useful_links form
class UsefulLinksForm(BaseForm):
    model = UsefulLinks
    template_name = "admin/banner/form.html"
    success_url = "useful_links_list"
    image_field = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Полезные ссылки"
        context["model_name"] = UsefulLinks.__name__
        context["list_url"] = "useful_links_list"
        context["app_name"] = "main"

        return context
