from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chess(request):
    return HttpResponse('chess is a easy game')

def abc(request):
    return HttpResponse('abc is good')