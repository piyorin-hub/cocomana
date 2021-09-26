from django.shortcuts import render
from django.http import HttpResponse
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append( str(current_dir) + '\\users' )
from models import Places, Evals

# Create your views here.
def add_space(request):
    #if request.method == 'POST':
    return HttpResponse(request.user.id)