from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('dhoni is a best finisher')