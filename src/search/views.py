from django.shortcuts import render
from users.models import Places

def index(request):
    return render(request, "search/index.html",{
        "places": Places.objets.all()
    })
# Create your views here.


