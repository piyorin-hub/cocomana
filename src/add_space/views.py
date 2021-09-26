from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_space(request):
    return HttpResponse("Hello, world!")