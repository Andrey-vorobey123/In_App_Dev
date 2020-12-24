from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^TheShRe/$', views.film1, name='film1'),
    url(r'^TheGrM/$', views.film2, name='film2'),
    url(r'^Tlotr/$', views.film3, name='film3'),
]