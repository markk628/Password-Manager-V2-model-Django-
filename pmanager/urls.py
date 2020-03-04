from django.urls import path
from pmanager.views import PlatformDetailView, PlatformListView, CreateNewPlatform, deletePlatform

urlpatterns = [
    path('', PlatformListView.as_view(), name='platform-list-page'),
    path('<int:pk>/', PlatformDetailView.as_view(), name='platform-detail-page'),
    path('create/', CreateNewPlatform.as_view(), name='platform-create-page'),
    path('<int:pk>/delete', deletePlatform, name='platform-delete'),
]