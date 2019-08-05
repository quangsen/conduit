from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from .models import Profile


class ProfileRetrieveAPIView(RetrieveAPIView):
    # queryset = Profile.objects.select_related('user')
    pass


class ProfileFollowAPIView(APIView):
    pass