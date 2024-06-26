from admins.forms import LngForm, UserForm
from custom.views import BasedListView, BaseForm
from admins.models import StaticInformation
from django.contrib.auth.models import User
from custom.models import Languages
from custom.utils import *
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import redirect
from django.db.models import Q



# static update
class StaticUpdate(BaseForm):
    model = StaticInformation
    fields = "__all__"
    template_name = 'admin/static_add.html'
    success_url = 'static_info'


    def get(self, request, *args, **kwargs):
        k = self.model._meta.verbose_name
        keys = [f'{k}_image', f'{k}_icon']
        predelete_image(keys, self.request, self.get_object().id)
        return super().get(request, *args, **kwargs)

    def get_object(self):
        try:
            object = StaticInformation.objects.get(id=1)
        except:
            object = StaticInformation.objects.create()

        return object

    def get_request_data(self):
        data_dict = super().get_request_data()
        cotalog = self.request.FILES.get("catalog")
        certificates = self.request.FILES.get("certificates")
        tech_info = self.request.FILES.get("tech_info")

        if cotalog:
            data_dict['catalog'] = cotalog

        if tech_info:
            data_dict['tech_info'] = tech_info

        if certificates:
            data_dict['certificates'] = certificates

        return data_dict
    

# super users list
class AdminsList(BasedListView):
    model = User
    template_name = 'admin/moterators_list.html'

    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=True)
        query = self.request.GET.get("q", '')

        if query != '':
            queryset = queryset.filter(Q(username__iregex=query) | Q(
                first_name__iregex=query) | Q(last_name__iregex=query))

        return queryset


# super user create
class AdminCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = '/'
    template_name = 'admin/moder_form.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_superuser = True
        full_name = self.request.POST.get("name")

        if full_name:
            full_name = full_name.split(' ')
            if len(full_name) > 0:
                new_user.first_name = full_name[0]

            if len(full_name) == 2:
                new_user.last_name = full_name[1]

        new_user.save()

        return redirect('admin_list')


# admin udate
class AdminUpdate(UpdateView):
    model = User
    form_class = UserForm
    success_url = '/'
    template_name = 'admin/moder_form.html'

    def get_context_data(self, **kwargs):
        context = super(AdminUpdate, self).get_context_data(**kwargs)
        context['full_name'] = ""

        if self.get_object().first_name:
            context['full_name'] = self.get_object().first_name + " "

        if self.get_object().last_name:
            context['full_name'] += self.get_object().last_name

        return context

    def form_valid(self, form):
        user = form.save()
        user.is_superuser = True
        full_name = self.request.POST.get("name")

        if full_name:
            if len(full_name.split(' ')) > 0:
                user.first_name = full_name.split(' ')[0]

            if len(full_name.split(' ')) == 2:
                user.last_name = full_name.split(' ')[1]

        user.save()

        return redirect('admin_list')


# del lang icond
def del_lang_icon(request):
    id = request.POST.get("item_id")
    url = request.POST.get('url')
    try:
        Languages.objects.get(id=int(id)).icon.delete()
    except:
        pass

    return redirect(url)

# add static image


def add_static_image(request):
    url = request.POST.get('url')
    key = request.POST.get("key")
    file = request.FILES.get('file')

    try:
        model = StaticInformation.objects.get(id=1)

        if key == 'logo1':
            model.logo_first = file
        elif key == 'logo2':
            model.logo_second = file

        model.save()
    except:
        pass

    return redirect(url)


# delete article images
def del_statics_image(request):
    url = request.POST.get('url')
    key = request.POST.get("key")

    try:
        model = StaticInformation.objects.get(id=1)

        if key == 'logo1':
            model.logo_first.delete()
        elif key == 'logo2':
            model.logo_second.delete()
        elif key == 'catalog':
            model.catalog.delete()
        elif key == 'certificates':
            model.certificates.delete()
        elif key == 'tech_info':
            model.tech_info.delete()

        model.save()
    except:
        pass

    return redirect(url)


# langs list
class LangsList(ListView):
    model = Languages
    context_object_name = 'langs'
    template_name = 'admin/lang_list.html'

    def get_queryset(self):
        queryset = Languages.objects.all().order_by('-default')
        query = self.request.GET.get("q")
        if query == '':
            query = None

        if query:
            queryset = queryset.filter(
                Q(name__iregex=query) | Q(code__iregex=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LangsList, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q")

        paginator = paginate(self.get_queryset(), self.request, 20)

        context['langs'] = get_lst_data(self.get_queryset(), self.request, 20, paginator)
        context['page_obj'] = paginator
        context['page_range'] = paginator.paginator.get_elided_page_range(
            number=paginator.number, on_each_side=3, on_ends=2)
        
        context['url'] = search_pagination(self.request)

        return context


# langs create
class LngCreateView(CreateView):
    model = Languages
    form_class = LngForm
    success_url = '/admin/langs'
    template_name = "admin/lng_create.html"

    def form_valid(self, form):
        lang_save(form, self.request)

        return redirect('langs_list')

    def get_context_data(self, **kwargs):
        context = super(LngCreateView, self).get_context_data(**kwargs)
        context['dropzone_key'] = self.model._meta.verbose_name
        context['images'] = []

        if self.request.session.get(context['dropzone_key']):
            context['images'] = list({'name': it['name'], 'id': clean_text(str(
                it['name']))} for it in self.request.session[context['dropzone_key']] if it['id'] == '')

        return context


# langs update
class LangsUpdate(UpdateView):
    model = Languages
    form_class = LngForm
    success_url = '/admin/langs'
    template_name = "admin/lng_create.html"

    def get_context_data(self, **kwargs):
        context = super(LangsUpdate, self).get_context_data(**kwargs)
        context['dropzone_key'] = self.model._meta.verbose_name

        return context

    def form_valid(self, form):
        lang_save(form, self.request)

        return redirect('langs_list')


# langs delete
def delete_langs(request):
    if request.method == 'POST':
        lng_id = request.POST.get("id")
        try:
            Languages.objects.get(id=int(lng_id)).delete()
        except:
            pass

        url = request.POST.get("url", request.META.get('HTTP_REFERER'))

        return redirect(url)
