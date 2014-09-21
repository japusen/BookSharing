from django.conf.urls import patterns, url

from content import views

urlpatterns = patterns('',
    url(r'^home/$', views.index, name='index'),
)