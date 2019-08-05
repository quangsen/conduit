from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'runcode'

urlpatterns = [
    url(r'^$', views.index_runcode, name='index_runcode'),
]
