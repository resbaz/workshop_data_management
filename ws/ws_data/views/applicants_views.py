from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Applicants
from ..forms import ApplicantsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ApplicantsListView(ListView):
    model = Applicants
    template_name = "ws_data/applicants_list.html"
    paginate_by = 20
    context_object_name = "applicants_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ApplicantsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ApplicantsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ApplicantsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ApplicantsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ApplicantsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ApplicantsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ApplicantsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ApplicantsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ApplicantsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ApplicantsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ApplicantsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ApplicantsListView, self).get_template_names()


class ApplicantsDetailView(DetailView):
    model = Applicants
    template_name = "ws_data/applicants_detail.html"
    context_object_name = "applicants"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ApplicantsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ApplicantsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ApplicantsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ApplicantsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ApplicantsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ApplicantsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ApplicantsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ApplicantsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ApplicantsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ApplicantsDetailView, self).get_template_names()


class ApplicantsCreateView(CreateView):
    model = Applicants
    form_class = ApplicantsForm
    fields = ['workshop', 'person', 'applicationDate', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/applicants_create.html"
    success_url = reverse_lazy("applicants_list")

    def __init__(self, **kwargs):
        return super(ApplicantsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ApplicantsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ApplicantsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ApplicantsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ApplicantsCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ApplicantsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ApplicantsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ApplicantsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ApplicantsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ApplicantsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ApplicantsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ApplicantsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ApplicantsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("applicants_detail", args=(self.object.pk,))


class ApplicantsUpdateView(UpdateView):
    model = Applicants
    form_class = ApplicantsForm
    fields = ['workshop', 'person', 'applicationDate', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/applicants_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "applicants"

    def __init__(self, **kwargs):
        return super(ApplicantsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ApplicantsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ApplicantsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ApplicantsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ApplicantsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ApplicantsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ApplicantsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ApplicantsUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ApplicantsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ApplicantsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ApplicantsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ApplicantsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ApplicantsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ApplicantsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ApplicantsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ApplicantsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ApplicantsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("applicants_detail", args=(self.object.pk,))


class ApplicantsDeleteView(DeleteView):
    model = Applicants
    template_name = "ws_data/applicants_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "applicants"

    def __init__(self, **kwargs):
        return super(ApplicantsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ApplicantsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ApplicantsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ApplicantsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ApplicantsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ApplicantsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ApplicantsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ApplicantsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ApplicantsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ApplicantsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ApplicantsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("applicants_list")
