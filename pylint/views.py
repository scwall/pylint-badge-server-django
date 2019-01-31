# Create your views here.
import jwt
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from pylint.models import ConventionPep8
from pylint.pylint_generator import PylintGenerator
from pylint.serializers import ReportsSerializer
from pylint_badge_server.settings import SECRET_KEY
from users.models import Repository, Reports


class ReportsView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                public_token = jwt.decode(self.request.data['public_token'], SECRET_KEY, algorithms=['HS256'])
            except jwt.InvalidSignatureError:
                return Response({'reports': 'Signature token, verification failed'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.InvalidTokenError:
                return Response({'reports': 'Invalid token. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                pylint_report = json.loads(self.request.data['pylint_report'].read().decode('utf-8'))
            except ValueError:
                return Response({'reports': 'report json file is not valid'}, status=status.HTTP_400_BAD_REQUEST)
            repository = Repository.objects.get(user_id=public_token['user_id'], id=int(public_token['repository_id']))
            if repository:
                pylint_generator = PylintGenerator(pylint_report)
                repository.badge.save(repository.name + ".svg", ContentFile(pylint_generator.get_svg))
                for report in pylint_generator.get_convention:
                    if ConventionPep8.objects.get(message_id=report['message-id']):
                        Reports.objects.create(line=report['line'],
                                               path=report['path'],
                                               column=report['column'],
                                               module=report['module'],
                                               obj=report['obj'],
                                               )

                return Response({'reports': 'received successful'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'reports': 'report failed, token is corrupt'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
