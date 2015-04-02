from django.conf.urls import patterns, include

urlpatterns = patterns('',

    (r'^studentss/', include('ws_data.urls.students_urls')),  # NOQA
    (r'^organisations/', include('ws_data.urls.organisation_urls')),
    (r'^persons/', include('ws_data.urls.person_urls')),
    (r'^workshops/', include('ws_data.urls.workshop_urls')),
    (r'^helperss/', include('ws_data.urls.helpers_urls')),
    (r'^instructors/', include('ws_data.urls.instructor_urls')),
    (r'^applicantss/', include('ws_data.urls.applicants_urls')),
)
