from django.urls import path
from .views import *

urlpatterns = [
    path('main/', aboba, name='index'),
    path('delete/<int:id>', delete, name='delete')
]