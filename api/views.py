from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from pmanager.models import Platform
from api.serializers import PlatformSerializer


class PlatformList(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformDetail(RetrieveDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer