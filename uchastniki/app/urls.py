from django.urls import path
from .views import *

urlpatterns = [
    path('events', main, name='events'),
]
