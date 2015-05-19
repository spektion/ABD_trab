from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import ipdb


from clientes.forms import ClienteForm
from clientes.models import cliente, crm_cliente


def cliente_list(request):
   
    cliente_list = [[cliente.nome, cliente.nacionalidade, cliente.bi, cliente.telemovel] for cliente_list in cliente.objects.all()]
    context = {'cliente_list': cliente_list}
    return render(request, 'cliente_list.html', context)


def cliente_detail(request, cod_cliente):
  
    cliente = cliente.objects.filter(cod_cliente = cod_cliente).first()
    cliente_detail = [cliente.cod_cliente, cliente.crm_cliente]
    context = {'cliente_detail': cliente_detail}
    return render(request, 'cliente_detail.html', context)

def cliente_new(request):    
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        try:
        
            if form.is_valid():
 
                saved = form.save(commit=True)
                return HttpResponseRedirect("/clientes/" + str(saved.pk) + "/")

            else:
                
                print form.errors
        except ValueError:
            print "Errors validating..."
    else:
        
        form = ClienteForm()

   
    return render(request, 'cliente_new.html', {'form': form})

def cliente_update(request, cod_cliente):    

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        try:
            if form.is_valid():
               
                saved = form.save(commit=True)

                return HttpResponseRedirect("/cliente/" + str(saved.pk) + "/")

            else:
             
                print form.errors
                return render(request, 'cliente_update.html', {'form': form, 'cod_cliente':cod_cliente})
        except ValueError:      
            print "Errors validating..."          
    else:
        cliente = cliente.objects.filter(cod_cliente = cod_cliente).first()
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente_update.html', {'form': form, 'cod_cliente':cod_cliente})
    

def cliente_delete(request, cod_cliente):    
   
    cliente.objects.filter(cod_cliente = cod_cliente).delete()    
    return HttpResponseRedirect("/clientes/")


def index(request):    
   return HttpResponse("todas as outras paginas vem aqui parar...!")