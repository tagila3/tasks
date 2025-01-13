from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    envents = Event.objects.all()
    return render(request, 'index.html', {'events': envents})