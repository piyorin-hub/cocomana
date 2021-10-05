from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Places, Evals
from django.views import generic
from .forms import SaveForm, EvalsForm

def generateView(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SaveForm(request.POST, prefix = "place")
        if form.is_valid(): # All validation rules pass
            #if form.data.get("evals-concentrations")!="" and form.data.get("evals-silence")!="" and form.data.get("evals-cost_pafo")!="" and form.data.get("evals-conges")!="":
            #存在しているかのチェック同じものがあれば評価は消してupdata。評価追加
            place = form.save()
            place = Places.objects.get(place_name = place.place_name, open_time=place.open_time, close_time=place.close_time, prefecture=place.prefecture, municipal=place.municipal, place_address=place.place_address, wifi=place.wifi, charge=place.charge, personal_space=place.personal_space, place_cost=place.place_cost, place_category=place.place_category)
            #print("place",form.data)
            evals_form = Evals(place_id=place, user_id=request.user, concentrations=form.data.get("evals-concentrations"), silence=form.data.get("evals-silence"), cost_pafo=form.data.get("evals-cost_pafo"), conges=form.data.get("evals-conges"))
            evals = evals_form.save()
            return redirect('users:top')

    #else:
    place_form = SaveForm(prefix = "place")
    evals_form = EvalsForm(prefix = "evals")
    process_name = "スペースの追加"
    return render(request, 'add_space/add_space.html', {
        "place_form": place_form,
        "evals_form": evals_form,
        "process_name": process_name,
    })
