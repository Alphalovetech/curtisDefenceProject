from django.contrib import admin
from polling_app.models import voters, candidates

# Register your models here.
admin.site.register(voters)
admin.site.register(candidates)


from django.urls import path
from django.shortcuts import render

