from django.shortcuts import render
from users.models import Places, Evals
from django.db.models import Q

def index(request):
     queries = request.GET.get('q')
     evals = Evals.objects.values('place_id')
     i = Evals.objects.all()
     print(evals)
     if queries:
         if " " in queries or "　" in queries:
             queries = queries.split()
             for query in queries:
                places = Places.objects.all().order_by()
                places.append = places.filter(
                    Q(place_name__icontains=query)|
                    Q(wifi__icontains=query)|
                    Q(personal_space__icontains=query)|
                    Q(prefecture__icontains=query)|
                    Q(municipal__icontains=query)|
                    Q(place_address__icontains=query)
                    ).distinct()
             
         else:
             query = queries
             print(query)
             places = Places.objects.all().order_by()
             places = places.filter(
                 Q(place_name__icontains=query)|
                 Q(wifi__icontains=query)|
                 Q(personal_space__icontains=query)|
                 Q(prefecture__icontains=query)|
                 Q(municipal__icontains=query)|
                 Q(place_address__icontains=query)
                 ).distinct()
             print(places)

     else:
         query = queries
         places = Places.objects.all().order_by()
     place_id = Places.objects.values('place_id')
     print(Places.objects.values('place_id'))
     k = []
     for place in place_id:
         for eval in evals:
             if place == eval:
                 
                 k.append(eval)
                 print(k)
     print(k)            
     print(places)
     print(i)           
     return render(request, "search/index.html", {
         'places': places, 'query': query,
         'evals': i
     })
    
    
    
    
    # return render(request, "search/index.html",{
    #     "places": Places.objects.all()
    # })
# Create your views here.


