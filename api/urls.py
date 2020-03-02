from django.urls import path

from api.views import PlatformList, PlatformDetail

urlpatterns = [
    path('platform/', PlatformList.as_view(), name='platform_list'),
    path('platform/<int:pk>', PlatformDetail.as_view(), name='platform_detail')
]