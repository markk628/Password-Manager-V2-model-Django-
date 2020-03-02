from rest_framework.serializers import ModelSerializer

from pmanager.models import Platform

class PlatformSerializer(ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

