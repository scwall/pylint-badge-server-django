# Create your views here.
from django.http import Http404

from .models import CustomUser, Repository, Reports
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from users.serializers import CurrentUserSerializer, RepositorySerializer, ReportSerializer
from rest_framework import status

class RepositoryList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        repository = Repository.objects.filter(user=request.user).all()

        print(request.user.id)
        serializer =  RepositorySerializer(repository,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RepositorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RepositoryDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk,request):

        try:

            repository = Repository.objects.filter(user=request.user).get(pk=pk)
            report = Reports.objects.filter(repository=repository)



            return (repository,report)
        except Repository.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        repository,report = self.get_object(pk,request)
        serializerRepository = RepositorySerializer(repository)
        serializerReport = ReportSerializer(report,many=True)
        return Response({'repository':serializerRepository.data,
                         'report':serializerReport.data,
                         })


    def delete(self, request, pk, format=None):
        repository = self.get_object(pk,request)
        repository.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
