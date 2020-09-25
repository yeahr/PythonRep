from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index/index.html', {'str': 'hello'})


def strap(request):
    return render(request, 'index/strap.html')
