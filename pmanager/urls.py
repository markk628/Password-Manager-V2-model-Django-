from django.urls import path
from pmanager.views import PlatformDetailView, PlatformListView, CreateNewPlatform, deletePlatform, UpdatePlatform

urlpatterns = [
    path('', PlatformListView.as_view(), name='platform-list-page'),
    path('<int:pk>/', PlatformDetailView.as_view(), name='platform-detail-page'),
    path('create/', CreateNewPlatform.as_view(), name='platform-create-page'),
    path('(?P<pk>[0-9]+)/$/update/', UpdatePlatform.as_view(), name='platform-update-page'),
    path('<int:pk>/delete', deletePlatform, name='platform-delete'),
]