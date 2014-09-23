from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^checklogin/$', views.checklogin, name='checklogin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkValue/$', views.checkValue, name='checkValue'),
)