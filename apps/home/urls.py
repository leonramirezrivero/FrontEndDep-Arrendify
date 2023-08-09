# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),    
    # INQUILINO
    path('inquilinos/', views.path_inq, name='inquilinos'),    
    path('detalles_inquilino/<int:id>', views.path_inq_detalles, name='inquilinos_detalles'),    
    path('editar_inq/<int:id>', views.path_inq_edit, name='inquilinos_editar'),    
    path('documentos_inq/<int:id>', views.path_archivos_inq, name='archivos_inquilinos'),    
    path('detalles_documentos/<int:id>', views.path_detalles_archivos, name='detalles_archivos'),
    path('detalles_historial_ingresos/<int:id>', views.path_detalles_archivos_historial, name='detalles_historial_ingresos'),
    #FIADOR    
    path('fiador_obligado/', views.path_foo, name='fiador_obligado'),   
    path('detalles_fiador/<str:slug>', views.path_foo_detalles, name='inquilinos_detalles'),    
    path('editar_fiador/<str:slug>', views.path_foo_edit, name='inquilinos_editar'),   
    path('documentos_fia/<int:id>', views.path_archivos_fia, name='archivos_fiador'),    
    path('det_documentos/<int:id>', views.path_detalles_archivos_fia, name='detalles_archivos_fiador'),
    #TERMINOS
    path('tyc/', views.tyc, name='tyc'),
    path('cotizacion/', views.cotizacion, name='tyc'),
    #ARRENDADOR
    path('arrendadores/', views.path_arrendador, name='arren'),    
    path('editar_arrendador/<str:slug>/', views.path_arrendador_editar, name='arrendador_editar'),
    path('detalles_arrendador/<str:slug>/', views.path_arrendador_detalles, name='detalles_arrendador'),
    path('documentos_arrendadores/', views.path_documentos_arrendador, name='archivos_arrendador'), 
    path('documentos_detalles/', views.path_documentos_arrendador_detalles_nuevo_template, name='documentos_detalles'),
    path('documentos_detalles/<str:slug>/', views.path_documentos_arrendador_detalles_unico_arrendador, name='documentos_arrendador_unico'),          
    path('historial/<str:slug>/', views.path_documentos_arrendador_ver_historial, name='path_documentos_arrendador_ver_historial'), 
    #INMUEBLES
    path('inmuebles/', views.path_inmuebles, name='inmuebles'),
    path('editar_inmuebles/<str:slug>/', views.path_inmuebles_editar, name='inmuebles_editar'),       
    path('detalles_inmuebles/<str:slug>/', views.path_inmuebles_detalles, name='inmuebles_detalles'),
    #INVESTIGACION
    path('investigacion/', views.path_investigacion, name='investigacion'),
    path('checklist_investigacion/', views.path_check_investigacion, name='check_investigacion'),
    # Contraseña
    path('recuperar_password/', views.path_recuperar_contraseña, name="recuperar_contrasena"),
    path('guardar_password', views.path_guardar_nueva_contraseña, name="guardar_password/"),
    # Contactanos
    path('contactanos/', views.path_contactanos, name="contactanos"),
    # Preguntas Frecuentes
    path('preguntas_frecuentes/', views.path_preguntas_frecuentes, name="preguntas_frecuentes"),
    # Datos de arrendamiento
    path('datos_arrendamiento/', views.path_datos_arrendamiento, name="datos_arrendamiento"),
    # Validar arrendador
    path('validar_investigacion_arrendador/', views.path_validar_arrendador, name='validar_arrendador'),
    path('investigacion_arrendadores/', views.path_total_arrendadores, name="investigacion_arrendadores"),
    # Comentarios
    path('comentarios/', views.path_comentarios, name="comentarios"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
