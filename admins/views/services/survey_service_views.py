from service.models import SecondSurveyService
from custom.views import BasedListView, BaseForm


# SecondSurveyService list
class SecondSurveyServiceList(BasedListView):
    model = SecondSurveyService
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Сервисы"
        context["model_name"] = SecondSurveyService.__name__
        context["create_url"] = "service_create"
        context["edit_url"] = "service_edit"
        context["app_name"] = "service"

        return context


# activity category form
class SecondSurveyServiceForm(BaseForm):
    model = SecondSurveyService
    template_name = "admin/category/form.html"
    success_url = "service_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Сервисы"
        context["model_name"] = SecondSurveyService.__name__
        context["list_url"] = "service_list"
        context["app_name"] = "service"

        return context
