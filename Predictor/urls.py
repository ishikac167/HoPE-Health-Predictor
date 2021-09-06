from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
    path('PCOD/', views.PCOD, name='PCOD'),
    path('result_PCOD/', views.result_PCOD, name='result_PCOD'),
    # path('signup', views.Signup, name='signup')
]