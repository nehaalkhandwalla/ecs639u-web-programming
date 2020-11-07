from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, 'mainapp/index.html', {})

# health probe
def health(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
