from django.conf.urls import url
from . import views

app_name = 'badala'

urlpatterns = [

    #badala
    url(r'^$', views.UserFormView.as_view(), name='index'),
    #badala/consumption id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

