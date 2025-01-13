from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})