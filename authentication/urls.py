from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user/?$', views.index_auth, name='index_auth')
]
