from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'movies': ['gladiator', 'top gun', '007']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})