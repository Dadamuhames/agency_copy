from service.models import UserOpinion
from custom.views import BasedListView
from django.views.generic import DetailView


# user opinion list
class UserOpinionList(BasedListView):
    model = UserOpinion
    template_name = "admin/user_opinion/list.html"
    search_fields = ["first_name", "last_name", "phone", "email"]


# user opinion detail
class UserOpinionDetail(DetailView):
    model = UserOpinion
    template_name = "admin/user_opinion/detail.html"
