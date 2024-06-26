from custom.views import BasedListView, BaseForm
from main.models import CommunityCouncil


# CommunityCouncil list
class CommunityCouncilList(BasedListView):
    model = CommunityCouncil
    template_name = "admin/article/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Общественный совет"
        context["model_name"] = CommunityCouncil.__name__
        context["create_url"] = "community_council_create"
        context["edit_url"] = "community_council_edit"
        context['app_name'] = "main"

        return context


# CommunityCouncil form
class CommunityCouncilForm(BaseForm):
    model = CommunityCouncil
    template_name = "admin/article/form.html"
    success_url = "community_council_list"
    image_field = "image"
    exclude_fields = ['views', "created_at", "updated_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Общественный совет"
        context["model_name"] = CommunityCouncil.__name__
        context["list_url"] = "community_council_list"
        context["app_name"] = "main"

        return context
