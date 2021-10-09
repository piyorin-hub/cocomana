from django.db import connection, connections
from django.shortcuts import render, redirect
#from django.http import HttpResponse

from users.models import Places ,Evals ,Reviews
from add_space import forms
from django.db.models import Sum
#from django.views.generic import TemplateView
from django import forms
from django.views import generic
from .forms import SaveForm, EvalsForm

def generateView(request):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:login')
    if request.method == 'POST': # If the form has been submitted...
        form = SaveForm(request.POST)
        if form.is_valid(): # All validation rules pass
            place = Places.objects.get(place_id=1)
            review_form = Reviews(review_place_id=place, review_user_id=request.user, review_comment=form.data.get("review_comment"))
            evals_form = Evals(place_id=place, user_id=request.user, concentrations=form.data.get("concentrations"), silence=form.data.get("silence"), cost_pafo=form.data.get("cost_pafo"), conges=form.data.get("conges"))
            review = review_form.save()
            evals = evals_form.save()
            return redirect('space:index')

    
    review_form = SaveForm()
    evals_form = EvalsForm()
    process_name = "レビューの追加"
    return render(request, 'space/add_review.html', {
        "review_form": review_form,
        "evals_form": evals_form,
        "process_name": process_name,
    })


def index(request,placeid):
    space = Places.objects.get(place_id = placeid)
    
    reviews = Reviews.objects.filter(review_place_id = placeid).all()
    
    evals ={"concentrations":0, "silence":0, "cost_pafo":0, "conges":0}

    product_count = Evals.objects.filter(place_id = placeid).count()

    obj_1 = Evals.objects.filter(place_id = placeid).aggregate(concentrations = Sum('concentrations'))
    obj_2 = Evals.objects.filter(place_id = placeid).aggregate(silence = Sum('silence'))
    obj_3 = Evals.objects.filter(place_id = placeid).aggregate(cost_pafo = Sum('cost_pafo'))
    obj_4 = Evals.objects.filter(place_id = placeid).aggregate(conges = Sum('conges'))
    
    evals["concentrations"] = round( obj_1["concentrations"] / product_count)
    evals["silence"] = round( obj_2["silence"] / product_count)
    evals["cost_pafo"] = round( obj_3["cost_pafo"] / product_count)
    evals["conges"] = round( obj_4["conges"] / product_count)


    return render(request, "space/index.html",{
        'space':space,'evals':evals,'count':product_count,'reviews':reviews})
                    
        

