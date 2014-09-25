from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^checklogin/$', views.checklogin, name='checklogin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkValue/$', views.checkValue, name='checkValue'),
    url(r'^dept/$', views.deptlist, name='deptlist'),
    url(r'^dept/(?P<department>[A-Z]+)/$', views.classlist, name='classlist'),
    url(r'^dept/(?P<department>[A-Z]+)/(?P<course>[A-Z]+)/$', views.classlist, name='classlist'),
)