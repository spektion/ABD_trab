from django.db import models as md


class cliente(md.Model):
    """docstring for cliente"""
    nome = md.CharField(max_length=100, unique=True)
    cod_cliente = md.AutoField(primary_key=True)


class categoria(md.Model):
    """docstring for categoria"""
    cliente = md.ForeignKey(cliente, verbose_name="the related categoria Type")
    id = md.AutoField(primary_key=True)


class crm_cliente(md.Model):
    """docstring for crm_cliente"""
    name = md.CharField(max_length=100, unique=True) 
    id = md.AutoField(primary_key=True)
