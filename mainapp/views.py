from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, 'mainapp/index.html', {})

def health(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
