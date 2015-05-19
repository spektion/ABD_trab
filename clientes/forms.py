from django import forms
from clientes.models import cliente, categoria, crm_cliente



class ClienteForm(forms.ModelForm):
    cliente_location = forms.CharField(max_length=100)
    owner = forms.CharField(max_length=100)
    categoria = forms.ModelChoiceField(queryset=categoria.objects.all(), to_field_name="id")
    crm_cliente = forms.ModelChoiceField(queryset=crm_cliente.objects.all(), to_field_name="id")


