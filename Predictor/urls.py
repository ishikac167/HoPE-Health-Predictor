from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
    path('PCOD/', views.PCOD, name='PCOD'),
    path('result_PCOD/', views.result_PCOD, name='result_PCOD')
]