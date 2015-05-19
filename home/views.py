#-*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import ipdb




def index(request):   
    print "home index" 
    context = []
    return render(request, 'base.html', context)    


#def index(request):    
#   return HttpResponse("todas as outras paginas vem aqui parar...!")


def sign_in(request):

    # Set to False initially. registered changes value to True when registration succeeds.
    registered = False

    # Se for um POST estamos a processar dados que vêm do REQUEST.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        # Se o formulário vem bem preenchido...
        if user_form.is_valid():
            user = user_form.save()

            # set_password encripta a password enviada para colocar na BD.
            user.set_password(user.password)
            user.save()

            # Agora sim, o registo ficou feito e gravado.
            registered = True

        else:
            # They'll also be shown to the user.
            print user_form.errors

    #Nao sendo um post, estão a pedir o Formulário para preenchimento de um novo user
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'sign_in.html',
            {'user_form': user_form, 'registered': registered} )



def logging_in(request):

    # Set to False initially. registered changes value to True when registration succeeds.

    # Se for um POST estamos a processar dados que vêm do REQUEST.
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password") 


        user = authenticate(username=username, password=password)


        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")


    #Nao sendo um post, estão a pedir o Formulário para preenchimento de um novo user
    else:
        return  render(request, 'login.html')


def user_details(request):
    id_ = request.user.pk
    user_row = User.objects.filter(id = id_).first()
    user = [user_row.id, user_row.username, user_row.email]
    context = {'user': user}
    return render(request, 'user_details.html', context)


def user_logout(request):
    #Se está autenticado, faz logout
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/')




