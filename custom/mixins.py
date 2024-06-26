from django.shortcuts import render
from admins.models import MetaTags
from django.core.exceptions import ValidationError
from custom.utils import *
from django.views.generic.detail import SingleObjectTemplateResponseMixin, SingleObjectMixin
from django.views.generic.edit import ModelFormMixin
from django.http import JsonResponse


# get request data mixin
class GetRequestDataMixin(SingleObjectMixin):
    file_field = None
    image_field = None
    extra_images = []
    exclude_fields = []

    def get_id(self):
        obj = self.object
        id = ''
        if obj:
            id = obj.id

        return id


    # get images from request
    def get_request_files(self, data_dict):
        key = self.model._meta.verbose_name

        # get id
        id = self.get_id()        


        # get image keys list
        key_list = self.extra_images.copy()

        # if there is image field add it to keys list
        if self.image_field:
            key_list.append(key)

        # loop all image keys
        for item in key_list:
            if item == key:  # if image key is main key => image key does not change
                image_key = key
            else:
                image_key = f'{key}_{item}'  # else change image_key

            # get all files by key from session
            files = [it for it in self.request.session.get(
                image_key, []) if it['id'] == str(id)]

            if len(files):  # if there are files
                file = files[0]  # get first file

                if item == key:
                    data_dict[self.image_field] = file['name']
                else:
                    data_dict[item] = file['name']

        if self.file_field:
            file = self.request.FILES.get(self.file_field)

            if file:
                data_dict[self.file_field] = file

        return data_dict

    # get form data

    def get_request_data(self):
        data_dict = serialize_request(self.model, self.request)
        data_dict = self.get_request_files(data_dict)

        for field in self.exclude_fields:
            if field in data_dict:
                del data_dict[field]

        return data_dict



# custom view mixin
class CustomFormMixin(SingleObjectTemplateResponseMixin, ModelFormMixin, GetRequestDataMixin):
    related_model = None
    fields = '__all__'
    meta = False
    object = None
    observe_model = None

    def get_related_queryset(self):
        return self.related_model.objects.order_by("-id")

    def get_object(self, queryset=None):
        try:
            return super(CustomFormMixin, self).get_object(queryset)
        except AttributeError:
            return None

    # clean session
    def clean_data(self, key):
        id = self.get_id()
        clean_session(key, self.request, id=str(id))
        clean_session(f'{key}_multiple', self.request, str(id))

        if self.extra_images:
            for item in self.extra_images:
                clean_session(f'{key}_{item}', self.request, id=str(id))

    # form valid
    def form_isvalid(self, form):
        form.save()

        if self.observe_model:
            obj = self.get_object()

            if obj:
                self.observe_model.update()
            else:
                self.observe_model.create()

        if self.meta:
            meta_dict = serialize_request(MetaTags, self.request)

            meta = form.meta
            if meta is None:
                meta = MetaTags.objects.create()
                form.meta = meta
                form.save()

            try:
                for attr, value in meta_dict.items():
                    setattr(form.meta, attr, value)
                form.meta.save()
            except:
                pass

        return form

    # form error
    def form_error(self, data, error):
        if type(error) is ValidationError:
            error = error.message_dict
        elif type(error) is dict:
            error = error
        else:
            error = str(error)

        data['errors'] = error

        if self.meta:
            data['meta'] = serialize_request(MetaTags, self.request)

        if self.success_url and self.template_name:
            return render(self.request, self.template_name, context=data)
        else:
            return JsonResponse({'error': error}, status=403)


# multiple image mixin
class MultipleImageMixin(CustomFormMixin):
    multiple_image_model = None

    def form_isvalid(self, form):
        form = super().form_isvalid(form)

        key = self.model._meta.verbose_name  # get key for dropzone
        id = self.get_id()  # get id of instance or ""
        if self.multiple_image_model:

            files = self.request.session.get(f'{key}_multiple', [])

            for file in list(files):
                if file['id'] == str(id):
                    image = self.multiple_image_model(
                        parent=form, image=file['name'])
                    image.full_clean()
                    image.save()

        return form

    def form_error(self, data, error):
        if self.multiple_image_model:
            key = self.model._meta.verbose_name
            files = self.request.session.get(f'{key}_multiple', [])
            data['images'] = files
        return super().form_error(data, error)
