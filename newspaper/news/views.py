from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *


def index(request):
    news = Post.objects.all().order_by('dateCreation')
    return render(request, 'default.html', context={'news': news})

def details(request, pk):
    new = Post.objects.get(id=pk)
    return render(request, 'details.html', context={'new':new})
