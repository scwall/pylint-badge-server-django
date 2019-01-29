#!/usr/bin/python3
from rest_framework import routers

from .views import MainUser

router_users = routers.SimpleRouter()
router_users.register(r'users', MainUser)