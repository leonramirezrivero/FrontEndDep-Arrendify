# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render


def login(request):
    remote_ip = request.META.get('REMOTE_ADDR')
    print("IP VISITANTE LOGIN: ",remote_ip)
    return render(request, "accounts/login.html", {})

def registro(request):
    remote_ip = request.META.get('REMOTE_ADDR')
    print("IP VISITANTE REGISTER: ",remote_ip)
    return render(request, "accounts/register.html", {})
