from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('<slug:slug>/', views.detail, name='detail'),  # ← new
]