from django.shortcuts import render, get_object_or_404
from .models import MediaItem

def index(request):
    all_media = MediaItem.objects.exclude(rating__isnull=True).order_by('-rating', 'title')
    return render(request, 'movies/index.html', {'all_media': all_media})

def about(request):
    return render(request, 'movies/about.html')

def detail(request, slug):
    item = get_object_or_404(MediaItem, title__iexact=slug.replace('-', ' '))
    similar = MediaItem.objects.filter(
        category=item.category,
        rating__isnull=False
    ).exclude(pk=item.pk).order_by('-rating')[:12]

    return render(request, 'movies/detail.html', {
        'item': item,
        'similar': similar
    })

def watchlist(request):
    unwatched = MediaItem.objects.filter(watched=False).order_by('title')
    return render(request, 'movies/watchlist.html', {'unwatched': unwatched})