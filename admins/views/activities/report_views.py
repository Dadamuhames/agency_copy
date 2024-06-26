from activities.models import Report
from custom.views import BasedListView, BaseForm


# report list
class ReportsList(BasedListView):
    model = Report
    template_name = "admin/report/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Отчеты"
        context["model_name"] = Report.__name__
        context["create_url"] = "report_create"
        context["edit_url"] = "report_edit"
        context["app_name"] = "activities"

        return context


# report form
class ReportForm(BaseForm):
    model = Report
    template_name = "admin/report/form.html"
    success_url = "report_list"
    file_field = "file"
    exclude_fields = ["created_at", "updated_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Отчеты"
        context["model_name"] = Report.__name__
        context["list_url"] = "report_list"
        context["app_name"] = "activities"

        return context
