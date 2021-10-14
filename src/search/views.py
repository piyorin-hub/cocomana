from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from users.models import Places, Evals, Favo
from django.db.models import Q
from django.contrib import messages

def index(request):
     queries = request.GET.get('q')
     evals = Evals.objects.all()
     action = request.GET.get('action')
     
     if action == "silence":

         evals = Evals.objects.order_by('-silence')
     elif action == "concentrations":
         evals = Evals.objects.order_by('-concentrations')
     elif action == "cost_pafo":
         evals = Evals.objects.order_by('-cost_pafo')
     elif action == "conges":
         evals = Evals.objects.order_by('-conges')
     else:
         evals = Evals.objects.all()
     places = Places.objects.all()
     place_list =[]
     for eval in evals:
         for place in places:
             if eval == place:
                 place_list.append(place)



     print(f"a{place_list}")

     if queries:
         if " " in queries or "　" in queries:
             queries = queries.split()
             for query in queries:
                
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
     user_id = request.user
     favos = Favo.objects.values('favo_place_id').filter(favo_usr_id=user_id)
     print(f"aa{favos}")
     place_num = []
     for favo_place in favos.values():
         
         place_num.append(favo_place['favo_place_id_id'])
     
     print(place_num)         
     
     return render(request, "search/index.html", {
         'places': places, 'query': query,
         'evals': evals, 'favos':place_num
     })


def favorite(request, pk):
    print(f"場所 {pk}")
    place_obj = Places.objects.get(place_id=pk)
    print(place_obj)
    user = request.user
    
    favo_places = Favo.objects.filter(favo_place_id=place_obj, favo_usr_id=user)
    if not favo_places:
        print(f"お気に入り{favo_places}")

        favo = Favo(favo_place_id=place_obj, favo_usr_id=user)
        favo.save()
        return redirect("search:index")
    else:
        print("成功")
        favo_places.delete()
        favoo = True
        return redirect("search:index")

# class select(ListView):
#     templete_name = 'index.html'
#     model = Evals

#     def get_queryset(request, self, **kwargs):
#         return super().get_queryset(**kwargs)
# class favo_exist(ListView):

#     template_name = 'index.html'
#     model = Favo
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_id = self.request.user
#         place_id = self.request.GET.get('place_id')

#         context[""] = 
#         return context
    
    
    
    
    # return render(request, "search/index.html",{
    #     "places": Places.objects.all()
    # })
# Create your views here.


