from custom.views import BasedListView, BaseForm
from main.models import Advert
from custom.utils import predelete_image, clean_session
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from custom.models import Languages
from django.http import JsonResponse


# advert list
class AdvertList(BasedListView):
    model = Advert
    template_name = "admin/advert/list.html"
    search_fields = ["title"]


# ad form
class AdvertForm(BaseForm):
    model = Advert
    template_name = "admin/advert/form.html"
    success_url = "advert_list"

    def get_image_keys(self):
        keys = []
        key = self.model._meta.verbose_name
        langs = Languages.objects.filter(active=True)

        for lang in langs:
            keys.append({"key": f"{key}_{lang.code}", "lang": lang.code})

        return keys

    def get(self, request, *args, **kwargs):
        keys = [it["key"] for it in self.get_image_keys()]
        predelete_image(keys, self.request, str(self.get_id()))
        return super().get(request, *args, **kwargs)

    def get_images(self):
        keys = self.get_image_keys()
        id = self.get_id()

        images_data = {}
        obj = self.get_object()

        for image_key in keys:
            try:
                file = [
                    it
                    for it in self.request.session.get(image_key["key"], [])
                    if it["id"] == str(id)
                ][0].get("name", None)
            except:
                if obj and obj.image and obj.image.get(image_key["lang"]):
                    file = obj.image.get(image_key["lang"])
                else:
                    file = None

            images_data[image_key["lang"]] = file

        return images_data

    def get_request_data(self):
        data = super().get_request_data()
        data["image"] = self.get_images()
        return data

    def clean_data(self, key):
        keys = self.get_image_keys()

        for it in keys:
            clean_session(it["key"], self.request, str(self.get_id()))

        return super().clean_data(key)


# delete ad image
def delete_ad_image(request, pk):
    if request.method == "POST":
        lang = request.POST.get("lang", "")

        ad = get_object_or_404(Advert.objects.all(), id=int(pk))
        image_data = ad.image

        if image_data.get(lang, "") != "":
            image = image_data[lang]

            if default_storage.exists(image):
                default_storage.delete(image)

            image_data[lang] = ""

        ad.image = image_data
        ad.save()

        return JsonResponse({"message": "success"})
