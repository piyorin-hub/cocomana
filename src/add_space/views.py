from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Places, Evals
from django.views import generic
from .forms import SaveForm, EvalsForm

def generateView(request):
    if request.user.is_anonymous:#loginしていない場合勝手にloginページ
        return redirect('users:login')
    if request.method == 'POST': # If the form has been submitted...
        form = SaveForm(request.POST)
        if form.is_valid(): # All validation rules pass
            #存在しているかのチェック同じものがあれば評価は消してupdata。評価追加 municipal place_address
            Places.objects.filter(prefecture=form.data.get("prefecture"), municipal=form.data.get("municipal"), place_address=form.data.get("place_address")).delete()
            #同じ住所が存在しないからsave
            place = form.save()
            place = Places.objects.get(place_name = place.place_name, open_time=place.open_time, close_time=place.close_time, prefecture=place.prefecture, municipal=place.municipal, place_address=place.place_address, wifi=place.wifi, charge=place.charge, personal_space=place.personal_space, place_cost=place.place_cost, place_category=place.place_category)
            #print("place",form.data)
            evals_form = Evals(place_id=place, user_id=request.user, concentrations=form.data.get("concentrations"), silence=form.data.get("silence"), cost_pafo=form.data.get("cost_pafo"), conges=form.data.get("conges"))
            evals = evals_form.save()
            return redirect('users:top')

    
    place_form = SaveForm()
    evals_form = EvalsForm()
    process_name = "スペースの追加"
    return render(request, 'add_space/add_space.html', {
        "place_form": place_form,
        "evals_form": evals_form,
        "process_name": process_name,
    })
