from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import ipdb


from cliente.forms import clienteForm
from cliente.models import cliente, crm_cliente

# import logging
# logging.basicConfig()
# logger = logging.getLogger(__name__)


# Create your views here.
def cliente_list(request):
    '''O Controller (View no Django) deve ser fino! Quase sem codigo. 
    Deve controlar e aplicar filtragens simples'''
    
    cliente_list = [[cliente.cod_cliente, cliente.nacionalidade, cliente.bi, cliente.telemovel ] for cliente in cliente.objects.all()]
    context = {'cliente_list': cliente_list}
    return render(request, 'cliente_list.html', context)
