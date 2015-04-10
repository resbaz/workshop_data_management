from django.conf.urls import url, patterns

from .views import WorkshopList, WorkshopDetail, WorkshopCreate, WorkshopUpdate, WorkshopDelete

urlpatterns = patterns('',
    url(r'^', WorkshopList.as_view(), name='index'),
    url(r'^workshops/$', WorkshopList.as_view(), name='index'),
    url(r'^workshops/add/$', WorkshopCreate.as_view(), name='workshop_add'),
    url(r'^workshops/(?P<pk>[0-9]+)/$', WorkshopDetail.as_view(), name='workshop_detail'),
    url(r'^workshops/(?P<pk>[0-9]+)/update/$', WorkshopUpdate.as_view(), name='workshop_update'),
    url(r'^workshops/(?P<pk>[0-9]+)/delete/$', WorkshopDelete.as_view(), name='workshop_delete'),
)

