from custom.views import BasedListView, BaseForm
from service.models import Faq


# faq list
class FaqList(BasedListView):
    model = Faq
    template_name = 'admin/faq/list.html'
    search_fields = ['answer', 'question']


#  faq form
class FaqForm(BaseForm):
    model = Faq
    template_name = 'admin/faq/form.html'
    success_url = 'faq_list'
