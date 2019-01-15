#!/usr/bin/python3
from django.urls import path, include
from users.views import user, signup

app_name = 'users'
urlpatterns = [
    path('signup',signup,name='signup'),
    path('<str:username>',user,name='user'),
    path('oauth/', include('social_django.urls', namespace='social'))

]

