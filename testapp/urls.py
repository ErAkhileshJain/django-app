from django.conf.urls import url
from testapp import views

urlpatterns=[

    url(r'^hello$',views.helloWorld),
    url(r'^test',views.testing)
]