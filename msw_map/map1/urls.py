from django.conf.urls import patterns, url
from map1 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    #url(r'^/ajaxtest/$', views.ajaxtest, name='ajaxtest')
)