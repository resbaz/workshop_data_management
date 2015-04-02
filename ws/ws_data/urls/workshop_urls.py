from django.conf.urls import patterns, url
from ..views import (WorkshopListView, WorkshopCreateView, WorkshopDetailView,
                     WorkshopUpdateView, WorkshopDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(WorkshopCreateView.as_view()),
        name="workshop_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(WorkshopUpdateView.as_view()),
        name="workshop_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(WorkshopDeleteView.as_view()),
        name="workshop_delete"),

    url(r'^(?P<pk>\d+)/$',
        WorkshopDetailView.as_view(),
        name="workshop_detail"),

    url(r'^$',
        WorkshopListView.as_view(),
        name="workshop_list"),
)
