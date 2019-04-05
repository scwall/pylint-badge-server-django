#!/usr/bin/python3
from django.urls import path
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

from .views import ReportsView

router = routers.SimpleRouter()
urlpatterns = [
                  path('reports/', ReportsView.as_view()),

] + router.urls
# urlpatterns = format_suffix_patterns(urlpatterns)