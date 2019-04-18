from rest_framework import serializers
from .models import CustomUser, Repository, Reports


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
        model = Reports
        fields = ('line','path','column','module','obj','repository','content_type')