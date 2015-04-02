from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Helpers
from ..forms import HelpersForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class HelpersListView(ListView):
    model = Helpers
    template_name = "ws_data/helpers_list.html"
    paginate_by = 20
    context_object_name = "helpers_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HelpersListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HelpersListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HelpersListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HelpersListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HelpersListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HelpersListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HelpersListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HelpersListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HelpersListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HelpersListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HelpersListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HelpersListView, self).get_template_names()


class HelpersDetailView(DetailView):
    model = Helpers
    template_name = "ws_data/helpers_detail.html"
    context_object_name = "helpers"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(HelpersDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HelpersDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HelpersDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HelpersDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(HelpersDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(HelpersDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HelpersDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HelpersDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HelpersDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HelpersDetailView, self).get_template_names()


class HelpersCreateView(CreateView):
    model = Helpers
    form_class = HelpersForm
    fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/helpers_create.html"
    success_url = reverse_lazy("helpers_list")

    def __init__(self, **kwargs):
        return super(HelpersCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(HelpersCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HelpersCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HelpersCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(HelpersCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(HelpersCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HelpersCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HelpersCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(HelpersCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HelpersCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HelpersCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(HelpersCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HelpersCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("helpers_detail", args=(self.object.pk,))


class HelpersUpdateView(UpdateView):
    model = Helpers
    form_class = HelpersForm
    fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/helpers_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "helpers"

    def __init__(self, **kwargs):
        return super(HelpersUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HelpersUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HelpersUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HelpersUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HelpersUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(HelpersUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(HelpersUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(HelpersUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(HelpersUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HelpersUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HelpersUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(HelpersUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HelpersUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HelpersUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HelpersUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HelpersUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HelpersUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("helpers_detail", args=(self.object.pk,))


class HelpersDeleteView(DeleteView):
    model = Helpers
    template_name = "ws_data/helpers_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "helpers"

    def __init__(self, **kwargs):
        return super(HelpersDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HelpersDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HelpersDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HelpersDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HelpersDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(HelpersDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(HelpersDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HelpersDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HelpersDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HelpersDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HelpersDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("helpers_list")
