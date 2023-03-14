from django.urls import path 
from nikky.views import *
app_name='hai'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]