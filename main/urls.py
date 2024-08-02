from django.urls import path
from .views import *

urlpatterns = [
    path('main', show_home),
    path('', show_home)
]