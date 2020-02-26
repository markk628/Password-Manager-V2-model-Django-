from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from pmanager.models import Platform

# Create your views here.
class PlatformListView(ListView):
    model = Platform

    def get(self, request):
        platforms = self.get_queryset().all()
        return render(request, 'platformList.html', {
            'platforms': platforms
        })

class PlatformDetailView(DetailView):
    model = Platform

    def get(self, request, slug):
        platform = self.get_queryset().get(slug_iexact=slug)
        return render(request, 'platform.html', {
            'platform': platform
        })
