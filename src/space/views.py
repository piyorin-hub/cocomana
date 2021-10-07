from django.db import connection, connections
from django.shortcuts import render, redirect
#from django.http import HttpResponse

from users.models import Places ,Evals ,Reviews
from add_space import forms
from django.db.models import Sum
#from django.views.generic import TemplateView
from django import forms
from django.views import generic
from .forms import SaveForm

class SaveSpace(generic.edit.FormView):
    template_name = 'space/add_review.html'
    form_class =SaveForm

    def form_valid(self, form): #postの時の処理
        #print("form",form.data.get("place_name"))
        places = form.save() # formの情報を保存
        return redirect('space:index')
        

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "レビューの追加"
        return context

def index(request):
    space = Places.objects.get(place_id = 1)
    
    reviews = Reviews.objects.filter(review_place_id = 1).all()
    
    evals ={"concentrations":0, "silence":0, "cost_pafo":0, "conges":0}

    product_count = Evals.objects.filter(place_id = 1).count()

    obj_1 = Evals.objects.filter(place_id = 1).aggregate(concentrations = Sum('concentrations'))
    obj_2 = Evals.objects.filter(place_id = 1).aggregate(silence = Sum('silence'))
    obj_3 = Evals.objects.filter(place_id = 1).aggregate(cost_pafo = Sum('cost_pafo'))
    obj_4 = Evals.objects.filter(place_id = 1).aggregate(conges = Sum('conges'))
    
    evals["concentrations"] = round( obj_1["concentrations"] / product_count)
    evals["silence"] = round( obj_2["silence"] / product_count)
    evals["cost_pafo"] = round( obj_3["cost_pafo"] / product_count)
    evals["conges"] = round( obj_4["conges"] / product_count)


    return render(request, "space/index.html",{
        'space':space,'evals':evals,'count':product_count,'reviews':reviews})
                    
        

