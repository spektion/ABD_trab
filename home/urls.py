from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    #url(r'^.*sign_in.*$', views.index, name='index'),
    url(r'^.*$', views.index, name='index'),
)
