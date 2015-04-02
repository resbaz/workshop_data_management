from django.conf.urls import patterns, url
from ..views import (HelpersListView, HelpersCreateView, HelpersDetailView,
                     HelpersUpdateView, HelpersDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(HelpersCreateView.as_view()),
        name="helpers_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HelpersUpdateView.as_view()),
        name="helpers_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HelpersDeleteView.as_view()),
        name="helpers_delete"),

    url(r'^(?P<pk>\d+)/$',
        HelpersDetailView.as_view(),
        name="helpers_detail"),

    url(r'^$',
        HelpersListView.as_view(),
        name="helpers_list"),
)
