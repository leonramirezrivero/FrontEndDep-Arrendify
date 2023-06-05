# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),    
    path('inquilinos/', views.path_inq, name='inquilinos'),    
    path('detalles_inquilino/<int:id>', views.path_inq_detalles, name='inquilinos_detalles'),    
    path('editar_inq/<int:id>', views.path_inq_edit, name='inquilinos_editar'),    
    path('documentos_inq/<int:id>', views.path_archivos_inq, name='archivos_inquilinos'),    
    path('detalles_documentos/<int:id>', views.path_detalles_archivos, name='detalles_archivos'),
    path('detalles_historial_ingresos/<int:id>', views.path_detalles_archivos_historial, name='detalles_historial_ingresos'),


    path('inmuebles/', views.path_inmuebles, name='inmuebles'),   
    path('fiador_obligado/', views.path_foo, name='fiador_obligado'),   
    path('detalles_fiador/<str:slug>', views.path_foo_detalles, name='inquilinos_detalles'),    
    path('editar_fiador/<str:slug>', views.path_foo_edit, name='inquilinos_editar'),   
    path('tyc/', views.tyc, name='tyc'),



    path('arrendadores/', views.path_arrendador, name='arren'),    
    path('editar_arrendador/<str:slug>/', views.path_arrendador_editar, name='arrendador_editar'),
    path('detalles_arrendador/<str:slug>/', views.path_arrendador_detalles, name='detalles_arrendador'),


    path('inmuebles/', views.path_inmuebles, name='inmuebles'),
    path('editar_inmuebles/<str:slug>/', views.path_inmuebles_editar, name='inmuebles_editar'),       
    path('detalles_inmuebles/<str:slug>/', views.path_inmuebles_detalles, name='inmuebles_detalles'),
    # path('inmuebles/datos_inmueble/<str:slug>/', InmueblesViewSet.as_view({'get': 'datos_inmueble'}), name='datos_inmueble'),

    path('documentos_arrendadores/', views.path_documentos_arrendador, name='archivos_arrendador'), 
    # path('destroy_individual_archivos/<int:pk>/', DocumentosArrendadorViewSet.as_view({'delete': 'destroy_individual_archivos'}), name='destroy_individual_archivos'),
    # path('actualizar_archivos_individual/<int:pk>/', DocumentosArrendadorViewSet.as_view({'put': 'actualizar_archivos_individual'}), name='actualizar_archivos_individual'),

    path('documentos_detalles/', views.path_documentos_arrendador_detalles_nuevo_template, name='documentos_detalles'),
    path('documentos_detalles/<str:slug>/', views.path_documentos_arrendador_detalles_unico_arrendador, name='documentos_arrendador_unico'),          
    path('historial/<str:slug>/', views.path_documentos_arrendador_ver_historial, name='path_documentos_arrendador_ver_historial'), 

    path('documentos_fia/<int:id>', views.path_archivos_fia, name='archivos_fiador'),    
    path('det_documentos/<int:id>', views.path_detalles_archivos_fia, name='detalles_archivos_fiador'),
    path('tyc/', views.tyc, name='tyc'),
     
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
