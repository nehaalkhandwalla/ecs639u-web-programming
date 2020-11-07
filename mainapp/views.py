from django.shortcuts import render
from django.http import HttpResponse

from .models import PageView

# Create your views here.

def hello(request):
    return render(request, 'mainapp/index.html', {})

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())
