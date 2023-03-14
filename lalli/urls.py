from django.urls import path
from lalli.views import *
app_name='kamalakuru'
urlpatterns=[
    path('virat/',virat,name='virat'),
]