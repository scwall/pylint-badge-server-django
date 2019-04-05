# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet

from users.serializers import CurrentUserSerializer


class MainUser(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer

class ViewUser(APIView):
    def get(self, request, *args, **kwargs):
        return Response(request.user.username)

