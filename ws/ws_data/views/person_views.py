from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Person
from ..forms import PersonForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PersonListView(ListView):
    model = Person
    template_name = "ws_data/person_list.html"
    paginate_by = 20
    context_object_name = "person_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PersonListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PersonListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PersonListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PersonListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PersonListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PersonListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PersonListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PersonListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonListView, self).get_template_names()


class PersonDetailView(DetailView):
    model = Person
    template_name = "ws_data/person_detail.html"
    context_object_name = "person"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PersonDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonDetailView, self).get_template_names()


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    fields = ['name', 'other', 'email', 'dob', 'gender_identity']
    template_name = "ws_data/person_create.html"
    success_url = reverse_lazy("person_list")

    def __init__(self, **kwargs):
        return super(PersonCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PersonCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PersonCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(PersonCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PersonCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("person_detail", args=(self.object.pk,))


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    fields = ['name', 'other', 'email', 'dob', 'gender_identity']
    template_name = "ws_data/person_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "person"

    def __init__(self, **kwargs):
        return super(PersonUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PersonUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(PersonUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("person_detail", args=(self.object.pk,))


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "ws_data/person_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "person"

    def __init__(self, **kwargs):
        return super(PersonDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PersonDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PersonDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("person_list")
