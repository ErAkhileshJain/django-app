from django.conf.urls import url
from crud import views

urlpatterns = [
    url(r'^create$', views.create),
    url(r'^index$', views.index),
    url(r'^view$', views.view),
    url(r'^delete$', views.delete),
    url(r'^update$', views.update)
]
