# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 -Jonatan Sepulveda
"""

from django.contrib import admin


class RolesAdmin(admin.ModelAdmin):
      readonly_fields=('id','created','updated')


# Register your models here.
