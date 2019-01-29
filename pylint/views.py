# Create your views here.
import jwt
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from rest_framework import generics, mixins, status, schemas
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from pylint.pylint_badge import PylintSvg
from pylint.serializers import UserSerializer, ReportsSerializer
from pylint_badge_server.settings import SECRET_KEY
from users.models import Repository
from django.core import files


class ReportsView(APIView):

    def post(self, request,format=None,*args,**kwargs):
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                public_token = jwt.decode(self.request.data['public_token'], SECRET_KEY, algorithms=['HS256'])
            except jwt.InvalidSignatureError:
                return Response({'token': 'Signature verification failed'},status=status.HTTP_400_BAD_REQUEST)
            except jwt.InvalidTokenError:
                return Response({'token': 'Invalid token. Please try again.'},status=status.HTTP_400_BAD_REQUEST)
            travis_job_id = self.request.data['travis_job_id']
            pylint_report = self.request.data['pylint_report']
            print(public_token)
            repository = Repository.objects.get(id=int(public_token['repository_id']))
            pylint_svg = PylintSvg()
            pylint_svg.get_rating_and_colour(pylint_report)
            # repository_verification = Repository.user.objects(id=public_token['user_id'])

            # if repository_verification.id == repository.id:
            repository.badge.save(repository.name + ".svg", ContentFile(pylint_svg.get_svg) )

            return Response({'reports': 'received successful'},status=400)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
