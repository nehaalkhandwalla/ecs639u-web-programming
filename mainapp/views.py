from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, 'mainapp/index.html', {})

# health probe
def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())
