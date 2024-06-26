from custom.views import BasedListView, BaseForm
from main.models import Leadership


# leadership list
class LeadershipList(BasedListView):
    model = Leadership
    template_name = "admin/leadership/list.html"
    search_fields = ['title', 'phone_number']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Руководство"
        context['model_name'] = Leadership.__name__
        context["create_url"] = "leadership_create"
        context["edit_url"] = "leadership_edit"

        return context


# leadership form
class LeadershipForm(BaseForm):
    model = Leadership
    template_name = "admin/leadership/form.html"
    success_url = "leadership_list"
    image_field = "image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Руководство"
        context['model_name'] = Leadership.__name__
        context["list_url"] = "leadership_list"

        return context
