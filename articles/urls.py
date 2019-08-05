from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'articles'

router = DefaultRouter(trailing_slash=False)
# router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^article/feed/?$', views.ArticlesFeedAPIView.as_view())
]
