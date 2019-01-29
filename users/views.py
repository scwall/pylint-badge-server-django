# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet


class MainUser(ModelViewSet):
    queryset = User.objects.all()

    @action(detail=False)
    def count(self,request,**kwargs):
        queryset = User.objects.count()
        return Response({"count": queryset})