from HealthPredictor.views import PCOD, result_PCOD
from django.contrib import admin
from django.urls import path

import views

urlpatterns = [
    path('PCOD', PCOD, name='PCOD'),
    path('result_PCOD/', result_PCOD, name='result_PCOD')
]