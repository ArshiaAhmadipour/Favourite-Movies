from django.urls import path
from movies.views import *

urlpatterns = [
    path('', index),
    path('about/', about),
]