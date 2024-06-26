from activities.models import Activity, ActivityCategory
from custom.views import BasedListView, BaseForm


# ActivityCategory list
class ActivityCategoryList(BasedListView):
    model = ActivityCategory
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории деятельности"
        context["model_name"] = ActivityCategory.__name__
        context["create_url"] = "activity_category_create"
        context["edit_url"] = "activity_category_edit"
        context["app_name"] = "activities"

        return context


# activity category form
class ActivityCategoryForm(BaseForm):
    model = ActivityCategory
    template_name = "admin/category/form.html"
    success_url = "activity_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории деятельности"
        context["model_name"] = ActivityCategory.__name__
        context["list_url"] = "activity_category_list"
        context["app_name"] = "main"

        return context


# activity list
class ActivityList(BasedListView):
    model = Activity
    template_name = "admin/article/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Деятельность"
        context["model_name"] = Activity.__name__
        context["create_url"] = "activity_create"
        context["edit_url"] = "activity_edit"
        context["app_name"] = "activities"

        return context


# Activity form
class ActivityForm(BaseForm):
    model = Activity
    template_name = "admin/article/form.html"
    success_url = "activity_list"
    image_field = "image"
    exclude_fields = ["views", "created_at", "updated_at"]
    related_model = ActivityCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Деятельность"
        context["model_name"] = Activity.__name__
        context["list_url"] = "activity_list"
        context["app_name"] = "activities"

        return context
