# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('ISBN', models.CharField(serialize=False, primary_key=True, max_length=13)),
                ('Titulo', models.CharField(max_length=15)),
                ('Autor', models.CharField(max_length=100)),
                ('Editorial', models.CharField(max_length=100)),
                ('Pais', models.CharField(max_length=100)),
                ('anno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Fecha_Prestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_Devolucion', models.DateField()),
                ('Fecha_Devolucion_Real', models.DateField()),
                ('Libro', models.ForeignKey(to='blog.Libros')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('DPI', models.CharField(max_length=20)),
                ('NombreCompleto', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='Usuario',
            field=models.ForeignKey(to='blog.Usuario'),
        ),
    ]
