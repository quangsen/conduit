from django.shortcuts import render
from django.http import HttpResponse

def index_runcode(request):
    return HttpResponse('ok')
