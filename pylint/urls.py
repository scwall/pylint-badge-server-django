#!/usr/bin/python3
from django.urls import path

from pylint.views import main_page

app_name = 'pylint'
urlpatterns = [
    path('', main_page,name='main_page'),

]
