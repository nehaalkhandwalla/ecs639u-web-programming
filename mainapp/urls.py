from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import hello
from .views import simple_upload

urlpatterns = [
    path('', hello),
    url(r'^uploads/simple/$', simple_upload, name='simple_upload'),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

