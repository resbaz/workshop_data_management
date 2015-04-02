from django.conf.urls import patterns, url
from ..views import (ApplicantsListView, ApplicantsCreateView, ApplicantsDetailView,
                     ApplicantsUpdateView, ApplicantsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(ApplicantsCreateView.as_view()),
        name="applicants_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ApplicantsUpdateView.as_view()),
        name="applicants_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ApplicantsDeleteView.as_view()),
        name="applicants_delete"),

    url(r'^(?P<pk>\d+)/$',
        ApplicantsDetailView.as_view(),
        name="applicants_detail"),

    url(r'^$',
        ApplicantsListView.as_view(),
        name="applicants_list"),
)
