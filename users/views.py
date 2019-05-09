# Create your views here.
from django.http import Http404

from .models import CustomUser, Repository, Report, ReportPepRefactor, ReportPepError, ReportPepWarning, \
    ReportPepConvention
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from users.serializers import CurrentUserSerializer, RepositorySerializer, ReportSerializer, ReportDetailSerializer
from rest_framework import status

class RepositoryList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        repository = Repository.objects.filter(user=request.user).all()

        print(request.user.id)
        serializer = RepositorySerializer(repository, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RepositorySerializer(data=request.data,context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepositoryDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, request):

        try:

            repository = Repository.objects.filter(user=request.user).get(pk=pk)
            report_all = Report.objects.filter(repository=repository).all()
            report_last = report_all.all().last()
            print(report_all,report_last)
            ReportPepWarnings = ReportPepWarning.objects.filter(report=report_last).all()
            ReportPepConventions = ReportPepConvention.objects.filter(report=report_last).all()
            ReportPepErrors = ReportPepError.objects.filter(report=report_last).all()
            ReportPepRefactors = ReportPepRefactor.objects.filter(report=report_last).all()

            return (repository,report_all, report_last, ReportPepWarnings, ReportPepConventions, ReportPepErrors, ReportPepRefactors)
        except Repository.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        repository,report_all, report_last, ReportPepWarnings, ReportPepConventions, ReportPepErrors, ReportPepRefactors = self.get_object(
            pk, request)
        serializerRepository = RepositorySerializer(repository)
        serializerReportLast = ReportSerializer(report_last)
        serializerReportAll = ReportSerializer(report_all,many=True)
        serializerReportPepWarnings = ReportDetailSerializer(ReportPepWarnings, many=True)
        serializerReportPepConventions = ReportDetailSerializer(ReportPepConventions, many=True)
        serializerReportPepErrors = ReportDetailSerializer(ReportPepErrors, many=True)
        serializerReportPepRefactors = ReportDetailSerializer(ReportPepRefactors, many=True)

        return Response({'repository': serializerRepository.data,
                         'reportLast': serializerReportLast.data,
                         'reportAll': serializerReportAll.data,
                         'ReportPepWarnings': serializerReportPepWarnings.data,
                         'ReportPepConventions': serializerReportPepConventions.data,
                         'ReportPepErrors': serializerReportPepErrors.data,
                         'ReportPepRefactors': serializerReportPepRefactors.data,

                         })

    def delete(self, request, pk, format=None):
        repository = self.get_object(pk, request)
        repository.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
