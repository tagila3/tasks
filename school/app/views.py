from django.shortcuts import render, redirect
from .models import *

def index(request):
    directors = Director.objects.all()
    return render(request, 'index.html', {'directors':directors})


def delete(request, id):
    try:
        obj = School.objects.get(id=id)
    except:
        pass

    obj.delete()
    return redirect('main')