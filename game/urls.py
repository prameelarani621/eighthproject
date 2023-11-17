from game.views import *

from django.urls import path
app_name='ntg'

urlpatterns=[
 path('chess/',chess,name='chess'),
 path('abc/',abc,name='abc'),
]