from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
    path('PCOD/<slug:user_id>', views.PCOD, name='PCOD'),
    path('result_PCOD/<slug:user_id>', views.result_PCOD, name='result_PCOD'),
    path('DoctorInput/', views.DocInput, name='DoctorInput'),
    path('Doctor/', views.DocRecomm, name='Doctor'),
    path('HA/<slug:user_id>', views.HA, name='HA'),
    path('result_HA/<slug:user_id>', views.result_HA, name='result_HA'),
    # path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('signup/', views.signup, name='signup'),
    path('journal/', views.health_journal, name='journal'),
    path('updateuser/<slug:user_id>', views.updateuser, name='updateuser'),
    path('dashboard/<slug:user_id>', views.dashboard, name='dashboard')
]
