from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required

from .views import WorkshopList, WorkshopDetail, WorkshopCreate, WorkshopUpdate, WorkshopDelete, PersonList, PersonCreate, PersonDetail, InstitutionDetail, InstitutionList, InstitutionCreate, dashboard, institute_report, dashboard_csv, dashboard_swc

urlpatterns = patterns('',
    url(r'^$', dashboard, name='dashboard'),
    # THESE ARE COMMENTED OUT FOR PRIVACY/SECURITY REASONS
    #url(r'^$', WorkshopList.as_view(), name='index'),
    #    url(r'^workshops/$', WorkshopList.as_view(), name='workshop_index'),
    #url(r'^workshops/add/$', WorkshopCreate.as_view(), name='workshop_add'),
    #url(r'^workshops/(?P<slug>[-\w]+)/$', WorkshopDetail.as_view(), name='workshop_detail'),
    #url(r'^workshops/(?P<slug>[-\w]+)/update/$', WorkshopUpdate.as_view(), name='workshop_update'),
    #url(r'^workshops/(?P<slug>[-\w]+)/delete/$', WorkshopDelete.as_view(), name='workshop_delete'),
    #url(r'^people/$', login_required(PersonList.as_view()), name='person_index'),
    #url(r'^people/add/$', login_required(PersonCreate.as_view()), name='person_add'),
    #url(r'^people/(?P<slug>[-\w]+)/$', login_required(PersonDetail.as_view()), name='person_detail'),
    #url(r'^institutions/$', InstitutionList.as_view(), name='institution_index'),
    #url(r'^institutions/add/$', InstitutionCreate.as_view(), name='institution_add'),
    #url(r'^institutions/(?P<slug>[-\w]+)/$', InstitutionDetail.as_view(), name='institution_detail'),
    url(r'^reports/dashboard/$', dashboard, name='dashboard'),
    url(r'^reports/dashboard/swc/$', dashboard_swc, name='dashboard_swc'),
    url(r'^reports/dashboard/csv/$', dashboard_csv, name='dashboard_csv'),
    url(r'^reports/(?P<slug>[-\w]+)/$', institute_report, name='institution_reports'),
)

