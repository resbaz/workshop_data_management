from django.conf.urls import patterns, url
from ..views import (StudentsListView, StudentsCreateView, StudentsDetailView,
                     StudentsUpdateView, StudentsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(StudentsCreateView.as_view()),
        name="students_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StudentsUpdateView.as_view()),
        name="students_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StudentsDeleteView.as_view()),
        name="students_delete"),

    url(r'^(?P<pk>\d+)/$',
        StudentsDetailView.as_view(),
        name="students_detail"),

    url(r'^$',
        StudentsListView.as_view(),
        name="students_list"),
)
