from rest_framework import serializers
from .models import CustomUser, Repository, Report, ReportDetail


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('name', 'id', 'badge', 'public_token')
        read_only_fields = ('id', 'badge', 'public_token')

    def create(self, validated_data):
        print('create')
        print('user', self.context.get('user'))
        repository = Repository(
            name=validated_data['name'],
            user=self.context.get('user')
        )
        repository.save()
        return repository


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('number_report', 'score')


class ReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDetail
        fields = ('line', 'path', 'column', 'module', 'obj', 'message', 'message_id', 'symbol')
