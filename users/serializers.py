from rest_framework import serializers
from .models import CustomUser, Repository, Report


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name' )
class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('name',)
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('line','path','column','module','obj','content_type')