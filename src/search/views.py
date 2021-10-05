from django.shortcuts import render
from users.models import Places, Evals
from django.db.models import Q

def index(request):
     query = request.GET.get('q')
     

     if query:
       places = Places.objects.all().order_by()
       places = places.filter(
           Q(place_name__icontains=query)|
           Q(wifi__icontains=query)|
           Q(personal_space__icontains=query)|
           Q(prefecture__icontains=query)|
           Q(municipal__icontains=query)|
           Q(place_address__icontains=query)

       ).distinct()
     else:
         places = Places.objects.all().order_by()
     return render(request, "search/index.html", {
         'places': places, 'query': query,
         'evals': Evals.objects.all()
     })
    
    
    
    
    # return render(request, "search/index.html",{
    #     "places": Places.objects.all()
    # })
# Create your views here.


