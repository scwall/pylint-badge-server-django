#!/usr/bin/python3
from rest_framework import routers

# from .views import MainUser, ViewUser, MyTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users import views

#router_users = routers.SimpleRouter()
# router_users.register(r'users', MainUser)
urlpatternsuser = [
                    path('snippets/', views.SnippetList.as_view())
                  ]
