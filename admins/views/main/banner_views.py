from main.models import Banner
from custom.views import BasedListView, BaseForm


# banner list
class BannerList(BasedListView):
    model = Banner
    template_name = "admin/banner/list.html"
    search_fields = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Баннер"
        context["model_name"] = Banner.__name__
        context["create_url"] = "banner_create"
        context["edit_url"] = "banner_edit"
        context["app_name"] = "main"

        return context


# banner form
class BannerForm(BaseForm):
    model = Banner
    template_name = "admin/banner/form.html"
    success_url = "banner_list"
    image_field = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Баннер"
        context["model_name"] = Banner.__name__
        context["list_url"] = "banner_list"
        context["app_name"] = "main"

        return context
