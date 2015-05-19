from django.conf.urls import patterns, include, url
from clientes import views
from django.contrib import admin
from home import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/',include ('clientes.urls', namespace="clientes")),
    #url(r'Teste/$' , views.Teste),
    url(r'^home/?', include('home.urls', namespace="home")),
    url(r'^.*sign_in/?$', views.sign_in, name='sign_in'), 
    url(r'^.*login/?$', views.logging_in, name='login'), 
    url(r'^.*user_details/?$', views.user_details, name='user_details'), 
    url(r'^.*user_logout/?$', views.user_logout, name='user_logout'), 
    url(r'^.*/?$', include('home.urls', namespace="home")),
    )
