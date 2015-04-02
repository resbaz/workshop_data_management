from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Workshop
from ..forms import WorkshopForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class WorkshopListView(ListView):
    model = Workshop
    template_name = "ws_data/workshop_list.html"
    paginate_by = 20
    context_object_name = "workshop_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(WorkshopListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WorkshopListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WorkshopListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(WorkshopListView, self).get_queryset()

    def get_allow_empty(self):
        return super(WorkshopListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(WorkshopListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(WorkshopListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(WorkshopListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(WorkshopListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(WorkshopListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(WorkshopListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WorkshopListView, self).get_template_names()


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = "ws_data/workshop_detail.html"
    context_object_name = "workshop"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(WorkshopDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WorkshopDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WorkshopDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WorkshopDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(WorkshopDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(WorkshopDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(WorkshopDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WorkshopDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WorkshopDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WorkshopDetailView, self).get_template_names()


class WorkshopCreateView(CreateView):
    model = Workshop
    form_class = WorkshopForm
    fields = ['title', 'description', 'date_held', 'teaching_hours', 'catering']
    template_name = "ws_data/workshop_create.html"
    success_url = reverse_lazy("workshop_list")

    def __init__(self, **kwargs):
        return super(WorkshopCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(WorkshopCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WorkshopCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(WorkshopCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(WorkshopCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(WorkshopCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(WorkshopCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(WorkshopCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(WorkshopCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(WorkshopCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(WorkshopCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(WorkshopCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WorkshopCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("workshop_detail", args=(self.object.pk,))


class WorkshopUpdateView(UpdateView):
    model = Workshop
    form_class = WorkshopForm
    fields = ['title', 'description', 'date_held', 'teaching_hours', 'catering']
    template_name = "ws_data/workshop_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "workshop"

    def __init__(self, **kwargs):
        return super(WorkshopUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WorkshopUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(WorkshopUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(WorkshopUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WorkshopUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(WorkshopUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(WorkshopUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(WorkshopUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(WorkshopUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(WorkshopUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(WorkshopUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(WorkshopUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(WorkshopUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(WorkshopUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WorkshopUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WorkshopUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WorkshopUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("workshop_detail", args=(self.object.pk,))


class WorkshopDeleteView(DeleteView):
    model = Workshop
    template_name = "ws_data/workshop_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "workshop"

    def __init__(self, **kwargs):
        return super(WorkshopDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(WorkshopDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(WorkshopDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(WorkshopDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(WorkshopDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(WorkshopDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(WorkshopDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(WorkshopDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(WorkshopDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(WorkshopDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(WorkshopDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("workshop_list")
