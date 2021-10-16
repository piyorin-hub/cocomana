from django.db import connection, connections
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.views.generic.list import ListView
from users.models import Places ,Evals ,Reviews, Favo
from add_space import forms
from django.db.models import Sum
#from django.views.generic import TemplateView
from django.contrib import messages
from .forms import SaveForm, EvalsForm


def review(request, placeid):

    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:login')
    if request.method == 'POST': # If the form has been submitted...
        form = SaveForm(request.POST)
        if form.is_valid(): # All validation rules pass
            place = Places.objects.get(place_id=placeid)
            review_form = Reviews(review_place_id=place, review_user_id=request.user, review_comment=form.data.get("review_comment"))
            review = review_form.save()
            print("追加完了")
            return redirect('space:index', placeid=placeid)

    review_form = SaveForm()
    process_name = "レビューの追加"
    return render(request, 'space/add_review.html', {
        "review_form": review_form,
        "process_name": process_name,
    })


def evaluation(request, placeid):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:login')
    if request.method == 'POST': # If the form has been submitted...
        form = EvalsForm(request.POST)
        if form.is_valid(): # All validation rules pass
            place = Places.objects.get(place_id=placeid)
            evals_form = Evals(place_id=place, user_id=request.user, concentrations=form.data.get("concentrations"), silence=form.data.get("silence"), cost_pafo=form.data.get("cost_pafo"), conges=form.data.get("conges"))
            evals = evals_form.save()
            print("成功")
            return redirect('space:index', placeid=placeid)
    print("失敗")
    evals_form = EvalsForm()
    process_name = "評価する"
    return render(request, 'space/add_evaluation.html', {
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

    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return render(request, "space/index.html",{
            'space':space,'evals':evals,'count':product_count,'reviews':reviews})
    else:
        user_id = request.user
        favos = Favo.objects.values('favo_place_id').filter(favo_usr_id=user_id)
        print(f"aa{favos}")
        place_num = []
        for favo_place in favos.values():
            place_num.append(favo_place['favo_place_id_id'])
        print(place_num)
        return render(request, "space/index.html",{
            'space':space,'evals':evals,'count':product_count,'reviews':reviews,'favos':place_num})

    #return render(request, "space/index.html",{
            #'space':space,'evals':evals,'count':product_count,'reviews':reviews})
                   
        

def favorite(request, pk):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:login')

    print(f"場所 {pk}")
    place_obj = Places.objects.get(place_id=pk)
    print(place_obj)
    user = request.user

    favo_places = Favo.objects.filter(favo_place_id=place_obj, favo_usr_id=user)
    if not favo_places:
        print(f"お気に入り{favo_places}")

        favo = Favo(favo_place_id=place_obj, favo_usr_id=user)
        favo.save()
        return redirect('space:index', placeid=pk)
    else:
        print("成功")
        favo_places.delete()
        favoo = True
        return redirect('space:index', placeid=pk)