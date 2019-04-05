#!/usr/bin/python3
from rest_framework import routers

from .views import MainUser, ViewUser
from django.urls import path
router_users = routers.SimpleRouter()
router_users.register(r'users', MainUser)
urlpatternsuser = [
                  path('username/', ViewUser.as_view()),

] + router_users.urls