from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.static import serve 
from .settings import STATIC_ROOT

urlpatterns = [
    path('', include('backend.urls')),
    path('admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}), 
]
