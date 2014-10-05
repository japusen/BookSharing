from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^checklogin/$', views.checklogin, name='checklogin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkValue/$', views.checkValue, name='checkValue'),
    url(r'^dept/$', views.deptlist, name='deptlist'),
    url(r'^dept/(?P<department>[^/]+)/$', views.classlist, name='classlist'),
    url(r'^dept/(?P<department>[^/]+)/(?P<code>[0-9]+[A-Z]{0,5})/$', views.course, name='course'),
    url(r'^addBook/$', views.addBook, name='addBook'),
    url(r'^search/$', views.search, name='search'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^confirm/(?P<key>\w+)/', views.confirm, name='confirm'),
)