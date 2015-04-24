from django.conf.urls import url, patterns

from .views import WorkshopList, WorkshopDetail, WorkshopCreate, WorkshopUpdate, WorkshopDelete

urlpatterns = patterns('',
    url(r'^$', WorkshopList.as_view(), name='index'),
    url(r'^workshops/$', WorkshopList.as_view(), name='index'),
    url(r'^workshops/add/$', WorkshopCreate.as_view(), name='workshop_add'),
    url(r'^workshops/(?P<slug>[-_\w]+)/$', WorkshopDetail.as_view(), name='workshop_detail'),
    url(r'^workshops/(?P<slug>[-_\w]+)/update/$', WorkshopUpdate.as_view(), name='workshop_update'),
    url(r'^workshops/(?P<slug>[-_\w]+)/delete/$', WorkshopDelete.as_view(), name='workshop_delete'),
)

