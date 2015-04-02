from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Instructor
from ..forms import InstructorForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class InstructorListView(ListView):
    model = Instructor
    template_name = "ws_data/instructor_list.html"
    paginate_by = 20
    context_object_name = "instructor_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(InstructorListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstructorListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstructorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(InstructorListView, self).get_queryset()

    def get_allow_empty(self):
        return super(InstructorListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(InstructorListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(InstructorListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(InstructorListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(InstructorListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(InstructorListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(InstructorListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstructorListView, self).get_template_names()


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = "ws_data/instructor_detail.html"
    context_object_name = "instructor"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(InstructorDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstructorDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstructorDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstructorDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstructorDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(InstructorDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InstructorDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstructorDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstructorDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstructorDetailView, self).get_template_names()


class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/instructor_create.html"
    success_url = reverse_lazy("instructor_list")

    def __init__(self, **kwargs):
        return super(InstructorCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(InstructorCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstructorCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InstructorCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(InstructorCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(InstructorCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InstructorCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InstructorCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(InstructorCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstructorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InstructorCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(InstructorCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstructorCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("instructor_detail", args=(self.object.pk,))


class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorForm
    fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
    template_name = "ws_data/instructor_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "instructor"

    def __init__(self, **kwargs):
        return super(InstructorUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstructorUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InstructorUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InstructorUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstructorUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstructorUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(InstructorUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(InstructorUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(InstructorUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InstructorUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InstructorUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(InstructorUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InstructorUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InstructorUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstructorUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstructorUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstructorUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("instructor_detail", args=(self.object.pk,))


class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = "ws_data/instructor_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "instructor"

    def __init__(self, **kwargs):
        return super(InstructorDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InstructorDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(InstructorDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(InstructorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InstructorDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(InstructorDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(InstructorDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InstructorDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InstructorDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InstructorDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InstructorDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("instructor_list")
