from rest_framework import serializers
from .models import CustomUser, Repository, Report, ReportDetail


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name' )
class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('name','id')
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
            model = Report
            fields = ('number_report','score')
class ReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDetail
        fields = ('line','path','column','module','obj','pep8_type','message','message_id','symbol')