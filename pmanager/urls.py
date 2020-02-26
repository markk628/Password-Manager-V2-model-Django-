from django.urls import path
from pmanager.views import PlatformDetailView, PlatformListView

urlpatterns = [
    path('', PlatformListView.as_view(), name='platform-list-page'),
    path('<str:slug>/', PlatformDetailView.as_view(), name='platform-detail-page'),
]