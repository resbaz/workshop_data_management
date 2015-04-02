from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Organisation
from ..forms import OrganisationForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class OrganisationListView(ListView):
    model = Organisation
    template_name = "ws_data/organisation_list.html"
    paginate_by = 20
    context_object_name = "organisation_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(OrganisationListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganisationListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganisationListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(OrganisationListView, self).get_queryset()

    def get_allow_empty(self):
        return super(OrganisationListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(OrganisationListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(OrganisationListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(OrganisationListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(OrganisationListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(OrganisationListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganisationListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganisationListView, self).get_template_names()


class OrganisationDetailView(DetailView):
    model = Organisation
    template_name = "ws_data/organisation_detail.html"
    context_object_name = "organisation"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(OrganisationDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganisationDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganisationDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganisationDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganisationDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganisationDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(OrganisationDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganisationDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganisationDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganisationDetailView, self).get_template_names()


class OrganisationCreateView(CreateView):
    model = Organisation
    form_class = OrganisationForm
    fields = ['title', 'location', 'department']
    template_name = "ws_data/organisation_create.html"
    success_url = reverse_lazy("organisation_list")

    def __init__(self, **kwargs):
        return super(OrganisationCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(OrganisationCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganisationCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(OrganisationCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(OrganisationCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(OrganisationCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(OrganisationCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(OrganisationCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(OrganisationCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(OrganisationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(OrganisationCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(OrganisationCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganisationCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("organisation_detail", args=(self.object.pk,))


class OrganisationUpdateView(UpdateView):
    model = Organisation
    form_class = OrganisationForm
    fields = ['title', 'location', 'department']
    template_name = "ws_data/organisation_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "organisation"

    def __init__(self, **kwargs):
        return super(OrganisationUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganisationUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(OrganisationUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(OrganisationUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganisationUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganisationUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganisationUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(OrganisationUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(OrganisationUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(OrganisationUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(OrganisationUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(OrganisationUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(OrganisationUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(OrganisationUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganisationUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganisationUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganisationUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("organisation_detail", args=(self.object.pk,))


class OrganisationDeleteView(DeleteView):
    model = Organisation
    template_name = "ws_data/organisation_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "organisation"

    def __init__(self, **kwargs):
        return super(OrganisationDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(OrganisationDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(OrganisationDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(OrganisationDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(OrganisationDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(OrganisationDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(OrganisationDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(OrganisationDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(OrganisationDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(OrganisationDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(OrganisationDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("organisation_list")
