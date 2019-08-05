from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, status, viewsets


@api_view(['GET'])
def ArticleViewSet(request):
    pass


class ArticlesFeedAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Article.objects.get()