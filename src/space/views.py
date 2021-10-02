from django.db import connection, connections
from django.shortcuts import render
#from django.http import HttpResponse

from users.models import Places ,Evals ,Reviews
from . import forms
from django.db.models import Sum
#from django.views.generic import TemplateView
from django import forms

class NewReviewForm (forms.Form):
    id = forms.CharField(label="ユーザーid")
    review = forms.CharField(label="コメント")

def space(request):
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            review = form.cleaned_data["review"]
            i = Reviews(review_comment=review)
            i.save()
                
    space = Places.objects.get(place_id = 2)

    reviews = Reviews.objects.filter(review_place_id = 2).all()

    evals ={"concentrations":0, "silence":0, "cost_pafo":0, "conges":0}

    product_count = Evals.objects.filter(place_id = 2).count()

    obj_1 = Evals.objects.filter(place_id = 2).aggregate(concentrations = Sum('concentrations'))
    obj_2 = Evals.objects.filter(place_id = 2).aggregate(silence = Sum('silence'))
    obj_3 = Evals.objects.filter(place_id = 2).aggregate(cost_pafo = Sum('cost_pafo'))
    obj_4 = Evals.objects.filter(place_id = 2).aggregate(conges = Sum('conges'))
    
    evals["concentrations"] = round( obj_1["concentrations"] / product_count)
    evals["silence"] = round( obj_2["silence"] / product_count)
    evals["cost_pafo"] = round( obj_3["cost_pafo"] / product_count)
    evals["conges"] = round( obj_4["conges"] / product_count)


    return render(request, "space/index.html",{
        'space':space,'evals':evals,'count':product_count,'reviews':reviews,'form':NewReviewForm()})

