from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Students
from ..forms import StudentsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StudentsListView(ListView):
    model = Students
    template_name = "ws_data/students_list.html"
    paginate_by = 20
    context_object_name = "students_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StudentsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StudentsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StudentsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StudentsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StudentsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StudentsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StudentsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StudentsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StudentsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StudentsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StudentsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StudentsListView, self).get_template_names()


class StudentsDetailView(DetailView):
    model = Students
    template_name = "ws_data/students_detail.html"
    context_object_name = "students"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StudentsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StudentsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StudentsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StudentsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StudentsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StudentsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StudentsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StudentsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StudentsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StudentsDetailView, self).get_template_names()


class StudentsCreateView(CreateView):
    model = Students
    form_class = StudentsForm
    fields = ['workshop', 'person', 'grade', 'organisation', 'career_stage', 'attendance', 'dietary_requirements']
    template_name = "ws_data/students_create.html"
    success_url = reverse_lazy("students_list")

    def __init__(self, **kwargs):
        return super(StudentsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StudentsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StudentsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StudentsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StudentsCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(StudentsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StudentsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StudentsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StudentsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StudentsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StudentsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StudentsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StudentsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("students_detail", args=(self.object.pk,))


class StudentsUpdateView(UpdateView):
    model = Students
    form_class = StudentsForm
    fields = ['workshop', 'person', 'grade', 'organisation', 'career_stage', 'attendance', 'dietary_requirements']
    template_name = "ws_data/students_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "students"

    def __init__(self, **kwargs):
        return super(StudentsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StudentsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StudentsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StudentsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StudentsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StudentsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StudentsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StudentsUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(StudentsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StudentsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StudentsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StudentsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StudentsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StudentsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StudentsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StudentsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StudentsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("students_detail", args=(self.object.pk,))


class StudentsDeleteView(DeleteView):
    model = Students
    template_name = "ws_data/students_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "students"

    def __init__(self, **kwargs):
        return super(StudentsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StudentsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StudentsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StudentsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StudentsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StudentsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StudentsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StudentsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StudentsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StudentsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StudentsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("students_list")
