from django.conf.urls import url
from sites import views

urlpatterns=[

    url(r'^signin$',views.signin),
    url(r'^signup',views.signup),
    url(r'^logout$', views.sessionLogout),
    url(r'^$', views.home),

]