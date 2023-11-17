from colour.views import *

from django.urls import path
app_name='red'

urlpatterns=[
 path('black/',black,name='black'),
 path('clay/',clay,name='clay'),
]