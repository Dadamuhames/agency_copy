from service.models import InteractiveServices
from custom.views import BasedListView, BaseForm


# InteractiveServices list
class InteractiveServiceList(BasedListView):
    model = InteractiveServices
    template_name = "admin/interactive_service/list.html"
    search_fields = ['title']


# InteractiveServices form
class InteractiveServiceForm(BaseForm):
    model = InteractiveServices
    template_name = "admin/interactive_service/form.html"
    success_url = "interactive_service_list"
    image_field = "image"
