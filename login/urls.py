from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout)
]