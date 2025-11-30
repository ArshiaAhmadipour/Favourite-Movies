from django.shortcuts import render
from .models import MediaItem

def index(request):
    all_media = MediaItem.objects.exclude(rating__isnull=True).order_by('-rating', 'title')
    return render(request, 'movies/index.html', {'all_media': all_media})

def about(request):
    return render(request, 'movies/about.html')