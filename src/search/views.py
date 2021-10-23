from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from users.models import Places, Evals, Favo
from django.db.models import Q, Avg
from django.contrib import messages

def index(request):
    #  if request.user.is_anonymous:#loginしていない場合勝手にloginページ
    #     return redirect('users:login')
     queries = request.GET.get('q')
     evals = Evals.objects.all()
     place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges'))
     action = request.GET.get('action')
     
     if action == "silence":

         place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges')).order_by('-avg_silence')
         
     elif action == "concentrations":
         place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges')).order_by('-avg_concentrations')
     elif action == "cost_pafo":
         place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges')).order_by('-avg_cost_pafo')
     elif action == "conges":
         place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges')).order_by('-avg_conges')
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
             

     else:
         query = queries
         places = Places.objects.all().order_by()
     place_id = Places.objects.values('place_id')
     

    #  print(f"場所：{places}")
    #  evals_all = []
    #  for place in places:
    #      print(f"詳細：{place}")
     
     
     if request.user.is_anonymous:
        return render(request, "search/index.html", {
            'places': places, 'query': query,
            'evals': place_evals,
        })
     else: 
        user_id = request.user
        favos = Favo.objects.values('favo_place_id').filter(favo_usr_id=user_id)
        print(f"aa{favos}")
        place_num = []
        for favo_place in favos.values():
         
            place_num.append(favo_place['favo_place_id_id'])
     
        
         
     
        return render(request, "search/index.html", {
            'places': places, 'query': query,
            'evals': place_evals, 'favos':place_num
        })


def favorite(request, pk):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
         return redirect('users:login')

    print(f"場所 {pk}")
    place_obj = Places.objects.get(place_id=pk)
    print(place_obj)
    user = request.user
    
    favo_places = Favo.objects.filter(favo_place_id=place_obj, favo_usr_id=user)
    if not favo_places:
        

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


