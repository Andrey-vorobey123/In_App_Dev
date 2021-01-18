from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import url
from DZ import urls

urlpatterns = [
    
    url(r'^$', views.index, name='indexx'),
    url(r'^script/$', views.script.as_view(), name='script'),   
]