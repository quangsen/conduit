from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_auth(request):
    return HttpResponse('van quang')