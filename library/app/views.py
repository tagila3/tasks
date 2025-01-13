from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    librarys = Library.objects.all()
    return render(request, 'index.html', {'libs': librarys})