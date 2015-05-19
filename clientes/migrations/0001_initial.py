# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('nome', models.CharField(unique=True, max_length=100)),
                ('cod_cliente', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='crm_cliente',
            fields=[
                ('name', models.CharField(unique=True, max_length=100)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categoria',
            name='cliente',
            field=models.ForeignKey(verbose_name=b'the related categoria Type', to='clientes.cliente'),
            preserve_default=True,
        ),
    ]
