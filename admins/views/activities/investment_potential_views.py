from activities.models import InvestmentPotential
from custom.views import BaseForm


# InvestmentPotential form
class InvestmentPotentialForm(BaseForm):
    model = InvestmentPotential
    template_name = "admin/investment_potential.html"
    success_url = "investment_potential_view"
    image_field = "image"
    exclude_fields = ['created_at', "updated_at"]

    def get_object(self, queryset=None):
        instance, _ = InvestmentPotential.objects.get_or_create(id=1)
        return instance
