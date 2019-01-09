#!/usr/bin/python3
from django.urls import path

from pylint.views import main_page, reports

app_name = 'pylint'
urlpatterns = [
    path('', main_page,name='main_page'),
    path('reports',reports,name='reports'),
]
