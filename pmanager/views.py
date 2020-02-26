from django.shortcuts import render
from django.views.generic.detail import DetailView

from pmanager.models import Platform

# Create your views here.
class PlatformDetailView(DetailView):
    model = Platform

    def get(self, request, slug):
        platform = self.get_queryset().get(slug_iexact=slug)
        return render(request, 'platform.html', {
            'platform': platform
        })
