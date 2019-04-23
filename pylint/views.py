# Create your views here.
import jwt
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from pylint.pylint_generator import PylintGenerator
from pylint.serializers import ReportsSerializer
from pylint_badge_server.settings import SECRET_KEY
from users.models import Repository, Report, ReportDetail


class ReportsView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                public_token = jwt.decode(
                    self.request.data['public_token'], SECRET_KEY, algorithms=['HS256'])
            except jwt.InvalidSignatureError:
                return Response({'reports': 'Signature token, verification failed'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.InvalidTokenError:
                return Response({'reports': 'Invalid token. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                pylint_report = json.loads(
                    self.request.data['pylint_report'].read().decode('utf-8'))
            except ValueError:
                return Response({'reports': 'report json file is not valid'}, status=status.HTTP_400_BAD_REQUEST)
            repository = Repository.objects.filter(user_id=public_token['user_id'],
                                                   id=int(public_token['repository_id'])).first()

            if repository:
                report = Report.objects.filter(repository=repository).last()

                pylint_generator = PylintGenerator(pylint_report)
                repository.badge.save(
                    repository.name + ".svg", ContentFile(pylint_generator.get_svg))

                if report and report.number_report is 10:
                    Report.objects.filter(repository=repository).all().delete()
                    report = Report.objects.create(number_report=1, score=pylint_generator.get_rating,
                                                   repository=repository)
                elif report:
                    report = Report.objects.create(number_report=(report.number_report + 1),
                                                   score=pylint_generator.get_rating, repository=repository)
                else:
                    report = Report.objects.create(number_report=1,
                                                   score=pylint_generator.get_rating, repository=repository)
                print(report.id)
                print(report.number_report)
                for report_generator in pylint_generator.get_convention:
                    ReportDetail.objects.create(line=report_generator['line'],
                                                path=report_generator['path'],
                                                column=report_generator['column'],
                                                module=report_generator['module'],
                                                obj=report_generator['obj'],
                                                message=report_generator['message'],
                                                symbol=report_generator['symbol'],
                                                message_id=report_generator['message-id'],
                                                pep8_type="convention",
                                                report=report

                                                )
                for report_generator in pylint_generator.get_warning:
                    ReportDetail.objects.create(line=report_generator['line'],
                                                path=report_generator['path'],
                                                column=report_generator['column'],
                                                module=report_generator['module'],
                                                obj=report_generator['obj'],
                                                message=report_generator['message'],
                                                symbol=report_generator['symbol'],
                                                message_id=report_generator['message-id'],
                                                pep8_type="warning",
                                                report=report

                                                )
                for report_generator in pylint_generator.get_error:
                    ReportDetail.objects.create(line=report_generator['line'],
                                                path=report_generator['path'],
                                                column=report_generator['column'],
                                                module=report_generator['module'],
                                                obj=report_generator['obj'],
                                                message=report_generator['message'],
                                                symbol=report_generator['symbol'],
                                                message_id=report_generator['message-id'],
                                                pep8_type="error",
                                                report=report

                                                )
                for report_generator in pylint_generator.get_refactor:
                    ReportDetail.objects.create(line=report_generator['line'],
                                                path=report_generator['path'],
                                                column=report_generator['column'],
                                                module=report_generator['module'],
                                                obj=report_generator['obj'],
                                                message=report_generator['message'],
                                                symbol=report_generator['symbol'],
                                                message_id=report_generator['message-id'],
                                                pep8_type="refactor",
                                                report=report

                                                )
                return Response({'reports': 'received successful'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'reports': 'report failed, token is corrupt'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
