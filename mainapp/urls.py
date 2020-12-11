from django.urls import path

from .views import hello

urlpatterns = [
    path('', hello),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
]
