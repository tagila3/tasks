from django.shortcuts import render, redirect
from .models import *


def aboba(request):
    recipts = Recipe.objects.all()
    return render(request, 'index.html', {'recipts':recipts})

def delete(request, id):
    try:
        obj = Shef.objects.get(id=id)
    except:
        pass

    obj.delete()
    return redirect('index')