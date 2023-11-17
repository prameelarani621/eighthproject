from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def black(request):
    return HttpResponse('black i like that colour')

def clay(request):
    return HttpResponse('clay is a colour')