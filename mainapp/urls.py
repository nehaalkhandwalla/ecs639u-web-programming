from django.urls import path
from django.conf.urls import url

from .views import hello
from .views import simple_upload

urlpatterns = [
    path('', hello),
    url(r'^uploads/simple/$', simple_upload, name='simple_upload'),
]
