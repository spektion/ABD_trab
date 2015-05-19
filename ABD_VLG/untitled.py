from django.conf.urls import patterns, url
from clientes import views

urlpatterns= patterns('', 
	url(r'^Teste$', views.Teste, name= 'Teste'),)