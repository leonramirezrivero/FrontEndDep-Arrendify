# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from requests import get

from django.shortcuts import redirect, render, get_object_or_404

# //////////////////////////////////////
# paths 
# //////////////////////////////////////


def index(request):
    remote_ip = request.META.get('REMOTE_ADDR')
    print("IP VISITANTE INDEX: ",remote_ip)
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

#================INQUILINOS=================
def path_inq(request):
    return render(request, 'home/inquilinos/inquilinos.html', {
    })
def path_inq_detalles(request,id):
    return render(request, 'home/inquilinos/detalles_inquilino.html', {
    })
def path_inq_edit(request,id):
    return render(request, 'home/inquilinos/edit_inq.html', {
    })
def path_archivos_inq(request,id):
    return render(request, 'home/inquilinos/archivos_inquilino.html', {
    })
def path_detalles_archivos(request,id):
    return render(request, 'home/inquilinos/detalles_archivos.html', {
    })

def path_detalles_archivos_historial(request,id):
    return render(request, 'home/inquilinos/historial_documentos.html', {
    })
    
#================Arrendadors=================


def path_arrendador(request):
    return render(request, 'home/arrendador/arrendador.html', {
    })

def path_arrendador_editar(request,slug):
    return render(request, 'home/arrendador/edit_arr.html', {
})

def path_arrendador_detalles(request,slug):
    return render(request, 'home/arrendador/detalles-arrendador.html', {
})

# path archivos arrendador

def path_documentos_arrendador(request):
    return render(request, 'home/archivos_arrendador/documentos_arrendador.html',{    
    })

def path_documentos_arrendador_editar(request):
    return render(request, 'home/archivos_arrendador/documentos_editar.html',{    
    })

def path_documentos_arrendador_detalles(request):
    return render(request, 'home/archivos_arrendador/detalles_documentos.html',{    
    })


def path_documentos_arrendador_detalles_nuevo_template(request):
    return render(request, 'home/arrendador/detalles_archivos.html',{    
    })

def path_documentos_arrendador_detalles_unico_arrendador(request, slug):
    return render(request, 'home/arrendador/detalles_archivos.html',{    
    })

def path_documentos_arrendador_ver_historial(request, slug):
    return render(request, 'home/arrendador/historial_arrendador.html',{    
    })

#================FIADORES=================
def path_foo(request):
    return render(request, 'home/Fiador/FOO.html', {
    })
def path_foo_detalles(request,slug):
    return render(request, 'home/Fiador/detalles_foo.html', {
    })
def path_foo_edit(request,slug):
    return render(request, 'home/Fiador/edit_inq_foo.html', {
    })    
def path_archivos_fia(request,id):
    return render(request, 'home/Fiador/archivos_fiador.html', {
    })
def path_detalles_archivos_fia(request,id):
    return render(request, 'home/Fiador/detalles_archivos.html', {
    })
#================FIADORES===============

def tyc(request):
    return render(request, 'home/Terminos.html', {
    })
    

# path inmuebles
def path_inmuebles(request):
    return render(request, 'home/inmuebles/inmuebles.html', {
    })

def path_inmuebles_editar(request, slug):
    return render(request, 'home/inmuebles/edit_inmueble.html', {
    })

def path_inmuebles_detalles(request, slug):
    return render(request, 'home/inmuebles/detalles-inmueble.html', {
    })



def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
