from django.conf.urls import patterns, url
from ..views import (OrganisationListView, OrganisationCreateView, OrganisationDetailView,
                     OrganisationUpdateView, OrganisationDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(OrganisationCreateView.as_view()),
        name="organisation_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(OrganisationUpdateView.as_view()),
        name="organisation_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(OrganisationDeleteView.as_view()),
        name="organisation_delete"),

    url(r'^(?P<pk>\d+)/$',
        OrganisationDetailView.as_view(),
        name="organisation_detail"),

    url(r'^$',
        OrganisationListView.as_view(),
        name="organisation_list"),
)
