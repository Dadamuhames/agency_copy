from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from custom.utils import *
from django.contrib import messages
from django.views.generic.edit import ProcessFormView
from django.http import JsonResponse
from django.db import transaction
from rest_framework import pagination, response
from .mixins import  *
# Create your views here.


# pagination
class BasePagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return response.Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


# <== update or create view START ==>
class BaseForm(CustomFormMixin, ProcessFormView):

    def form_valid(self, form):
        return None

    def form_invalid(self, form):
        return None

    def get_object(self, queryset=None):
        try:
            return super(BaseForm, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        key = self.model._meta.verbose_name
        id = self.get_id()

        images_list = [key, f'{key}_multiple']
        if self.extra_images:
            for item in self.extra_images:
                images_list.append(f'{key}_{item}')

        predelete_image(images_list, request, id)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseForm,
                        self).get_context_data(**kwargs)

        if self.related_model is not None:
            context['relateds'] = self.get_related_queryset()

        context['dropzone_key'] = self.model._meta.verbose_name
        context['success_url'] = self.success_url

        return context

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        self.object = self.get_object()
        data_dict = self.get_request_data()
        data = self.get_context_data()
        instance = self.get_object()

        try:
            with transaction.atomic():
                if instance:
                    for attr, value in data_dict.items():
                        setattr(instance, attr, value)
                else:
                    instance = self.model(**data_dict)

                key = self.model._meta.verbose_name
                instance.full_clean()
                self.form_isvalid(instance)

                self.clean_data(key)

        except Exception as e:
            data['request_post'] = data_dict
            return self.form_error(data, e)

        if self.get_object():
            messages.add_message(request, messages.SUCCESS,
                                 'Обьект успешно обновлен')
        else:
            messages.add_message(request, messages.SUCCESS,
                                 'Обьект успешно создан')

        if self.success_url:
            return redirect(self.success_url)
        else:
            return JsonResponse({'message': 'success'})


# <== update or create view END ==>


# based list view
class BasedListView(ListView):
    search_fields = list()

    def search(self, queryset, fields: list, *args, **kwargs):
        query = self.request.GET.get("q", '')

        if query == '':
            return queryset

        end_set = set()
        for field in fields:
            qs = queryset.extra(where=[f'LOWER({field}) LIKE %s'], params=[
                                f'%{query.lower()}%'])
            for item in qs:
                end_set.add(item)

        queryset = list_to_queryset(list(end_set), self.model)

        return queryset

    def get_queryset(self):
        queryset = self.model.objects.order_by('-id')
        queryset = self.search(queryset, self.search_fields)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(BasedListView, self).get_context_data(**kwargs)

        paginator = paginate(self.get_queryset(), self.request, 20)

        context['objects'] = get_lst_data(
            self.get_queryset(), self.request, 20, paginator)

        context['page_obj'] = paginator
        context['page_range'] = paginator.paginator.get_elided_page_range(
            number=paginator.number, on_each_side=3, on_ends=2)

        context['url'] = search_pagination(self.request)

        return context


# tour extra information base forms
class RelationForm(BaseForm):
    url_prefix = ''
    parent_model = None
    url_path = ""
    parent_field_name = ""

    def get_parent_queryset(self):
        queryset = self.parent_model.objects.all()
        return queryset

    def get_parent_object(self):
        parent_queryset = self.get_parent_queryset()
        id = self.kwargs.get("parent", 0)
        tour = get_object_or_404(parent_queryset, id=int(id))
        return tour

    def get_request_data(self):
        data_dict = super().get_request_data()
        data_dict[self.parent_field_name] = self.get_parent_object()
        return data_dict

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.parent_field_name] = self.get_parent_object()
        return context

    def post(self, request, *args, **kwargs):
        self.success_url = f"/admin/{self.url_path}/{self.get_parent_object().id}#{self.url_prefix}"
        return super().post(request, *args, **kwargs)
