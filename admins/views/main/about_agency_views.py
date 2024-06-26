from main.models import AboutAgency
from custom.views import BaseForm


# about agency form
class AboutAgencyForm(BaseForm):
    model = AboutAgency
    template_name = "admin/about_agency.html"
    success_url = "about_agency"
    image_field = "image"

    def get_object(self, queryset=None):
        instance, _ = AboutAgency.objects.get_or_create(id=1)
        return instance