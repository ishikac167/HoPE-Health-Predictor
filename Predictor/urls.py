from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
    path('PCOD/', views.PCOD, name='PCOD'),
    path('result_PCOD/', views.result_PCOD, name='result_PCOD'),
    path('DoctorInput/', views.DocInput, name='DoctorInput'),
    path('Doctor/', views.DocRecomm, name='Doctor')
    # path('signup/', views.Signup, name='signup'),
    # path('login/', views.Login, name='login')
]