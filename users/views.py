# Create your views here.
from .models import CustomUser, Repository
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from users.serializers import CurrentUserSerializer, RepositorySerializer
from rest_framework import status

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Repository.objects.filter(user_id=1).all()
        print(snippets)
        serializer =  RepositorySerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RepositorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
