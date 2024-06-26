from activities.models import Vacansy
from custom.views import BasedListView, BaseForm


# report list
class VacansyList(BasedListView):
    model = Vacansy
    template_name = "admin/vacansy/list.html"
    search_fields = ["title"]


# Vacansy form
class VacansyForm(BaseForm):
    model = Vacansy
    template_name = "admin/vacansy/form.html"
    success_url = "vacansy_list"
    image_field = "image"
    exclude_fields = ["views", "created_at", "updated_at"]
