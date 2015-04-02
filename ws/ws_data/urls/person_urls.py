from django.conf.urls import patterns, url
from ..views import (PersonListView, PersonCreateView, PersonDetailView,
                     PersonUpdateView, PersonDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(PersonCreateView.as_view()),
        name="person_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PersonUpdateView.as_view()),
        name="person_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PersonDeleteView.as_view()),
        name="person_delete"),

    url(r'^(?P<pk>\d+)/$',
        PersonDetailView.as_view(),
        name="person_detail"),

    url(r'^$',
        PersonListView.as_view(),
        name="person_list"),
)
