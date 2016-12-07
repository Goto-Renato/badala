from django.conf.urls import url
from . import views

app_name = 'badala'

urlpatterns = [
    #register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #badala
    url(r'^$', views.IndexView.as_view(), name='index'),
    #badala/consumption id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #badala/consumption/add/
    url(r'^consumption/add/$', views.ConsumptionCreate.as_view(), name='consumption-add'),
    #badala/consumption/update/
    url(r'^consumption/(?P<pk>[0-9]+)/$', views.ConsumptionUpdate.as_view(), name='consumption-update'),
    #badala/consumption/delete/
    url(r'^consumption/(?P<pk>[0-9]+)/delete/$', views.ConsumptionDelete.as_view(), name='consumption-delete'),
]

