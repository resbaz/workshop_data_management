from django.conf.urls import patterns, url
from ..views import (InstructorListView, InstructorCreateView, InstructorDetailView,
                     InstructorUpdateView, InstructorDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(InstructorCreateView.as_view()),
        name="instructor_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(InstructorUpdateView.as_view()),
        name="instructor_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(InstructorDeleteView.as_view()),
        name="instructor_delete"),

    url(r'^(?P<pk>\d+)/$',
        InstructorDetailView.as_view(),
        name="instructor_detail"),

    url(r'^$',
        InstructorListView.as_view(),
        name="instructor_list"),
)
