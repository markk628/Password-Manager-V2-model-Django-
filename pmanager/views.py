from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import Http404

from pmanager.models import Platform
from .forms import PlatformForm

# Create your views here.
class PlatformListView(ListView):
    model = Platform

    def get(self, request):
        platforms = self.get_queryset().all()
        return render(request, 'platformList.html', {'platforms': platforms})

class PlatformDetailView(DetailView):
    model = Platform

    def get(self, request, slug):
        platform = self.get_queryset().get(slug=slug)
        return render(request, 'platform.html', {'platform': platform})

class CreateNewPlatform(CreateView):
    model = Platform

    def get(self, request):

        content = {'form': PlatformForm()}
        return render(request, 'create_new_platform.html', content)


    def post(self, request):
        form = PlatformForm(request.POST)
        if form.is_valid():
            platform = form.save(commit=False)
            platform.user = request.user
            platform.save()
            return HttpResponseRedirect(reverse('platform-detail-page', args=[platform.id]))


        content = {'form': PlatformForm()}
        return render(request, 'create_new_platform.html', content)


def deletePlatform(request, slug):
    apple = get_object_or_404(Platform, slug=slug)
    apple.delete()
    return HttpResponseRedirect(reverse('platform-list-page'))




