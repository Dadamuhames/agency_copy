from education.models import Education, EducationCategory, Book
from custom.views import BasedListView, BaseForm


# EducationCategory list
class EducationCategoryList(BasedListView):
    model = EducationCategory
    template_name = "admin/category/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории образования"
        context["model_name"] = EducationCategory.__name__
        context["create_url"] = "education_category_create"
        context["edit_url"] = "education_category_edit"
        context["app_name"] = "education"

        return context


# activity category form
class EducationCategoryForm(BaseForm):
    model = EducationCategory
    template_name = "admin/category/form.html"
    success_url = "education_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Категории образования"
        context["model_name"] = EducationCategory.__name__
        context["list_url"] = "education_category_list"
        context["app_name"] = "main"

        return context


# education list
class EducationList(BasedListView):
    model = Education
    template_name = "admin/article/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Образование"
        context["model_name"] = Education.__name__
        context["create_url"] = "education_create"
        context["edit_url"] = "education_edit"
        context["app_name"] = "education"

        return context


# education form
class EducationForm(BaseForm):
    model = Education
    template_name = "admin/article/form.html"
    success_url = "education_list"
    image_field = "image"
    exclude_fields = ["views", "created_at", "updated_at"]
    related_model = EducationCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Образование"
        context["model_name"] = Education.__name__
        context["list_url"] = "education_list"
        context["app_name"] = "education"

        return context


# books list
class BooksList(BasedListView):
    model = Book
    template_name = "admin/article/list.html"
    search_fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Книги"
        context["model_name"] = Book.__name__
        context["create_url"] = "books_create"
        context["edit_url"] = "books_edit"
        context["app_name"] = "education"

        return context


# books form
class BookForm(BaseForm):
    model = Book
    template_name = "admin/books/form.html"
    success_url = "books_list"
    image_field = "image"
    file_field = "file"
