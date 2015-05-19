from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from cliente import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/',include('clientes.urls', namespace = "clientes")),
    url(r'^.*$', RedirectView.as_view(url='/clientes/')),
)
