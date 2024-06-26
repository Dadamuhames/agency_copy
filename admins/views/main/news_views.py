from main.models import NewsCategory, News
from custom.views import BasedListView, BaseForm


# NewsCategory list
class NewsCategoryList(BasedListView):
    model = NewsCategory
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории новостей"
        context["model_name"] = NewsCategory.__name__
        context["create_url"] = "news_category_create"
        context["edit_url"] = "news_category_edit"
        context["app_name"] = "main"

        return context


# activity category form
class NewsCategoryForm(BaseForm):
    model = NewsCategory
    template_name = "admin/category/form.html"
    success_url = "news_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории новостей"
        context["model_name"] = NewsCategory.__name__
        context["list_url"] = "news_category_list"
        context["app_name"] = "main"

        return context


# news list
class NewsList(BasedListView):
    model = News
    template_name = "admin/article/list.html"
    search_fields = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Новости"
        context["model_name"] = News.__name__
        context["create_url"] = "news_create"
        context["edit_url"] = "news_edit"
        context["app_name"] = "main"

        return context


# news form
class NewsForm(BaseForm):
    model = News
    template_name = "admin/news/form.html"
    success_url = "news_list"
    related_model = NewsCategory
    image_field = "image"
    exclude_fields = ['views', "created_at", "updated_at"]
