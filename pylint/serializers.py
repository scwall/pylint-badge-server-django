from rest_framework import serializers
from django.contrib.auth.models import User


class ReportsSerializer(serializers.Serializer):
    public_token = serializers.CharField()
    pylint_report = serializers.FileField()

class UserSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'user_count')

    def get_user_count(self, obj):
        return obj.objects.latest('user')
