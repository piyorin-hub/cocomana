from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Places, Evals
from django.views import generic
from .forms import SaveForm, EvalsForm

# class SaveSpace(generic.edit.FormView):
#     template_name = 'add_space/add_space.html'
#     form_class =SaveForm

#     def form_valid(self, form): #postの時の処理
#         #print("form",form.data.get("place_name"))
#         places = form.save() # formの情報を保存
#         return redirect('users:top')

#     # データ送信
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["process_name"] = "スペースの追加"
#         return context



def generateView(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SaveForm(request.POST, prefix = "place")
        if form.is_valid(): # All validation rules pass
            #存在しているかのチェック同じものがあれば評価は消してupdata。評価追加
            place = form.save()
            place = Places.objects.get(place_name = place.place_name, open_time=place.open_time, close_time=place.close_time, prefecture=place.prefecture, municipal=place.municipal, place_address=place.place_address, wifi=place.wifi, charge=place.charge, personal_space=place.personal_space, place_cost=place.place_cost, place_category=place.place_category)
            print("place",form.data)
            evals_form = Evals(place_id=place, user_id=request.user, concentrations=form.data.get("score")[0], silence=form.data.get("score")[1], cost_pafo=form.data.get("score")[2], conges=form.data.get("score")[3])
            evals = evals_form.save()
            return redirect('users:top')

    else:
        place_form = SaveForm(prefix = "place")
        evals_form = EvalsForm(prefix = "evals")
    process_name = "スペースの追加"
    return render(request, 'add_space/add_space.html', {
        "place_form": place_form,
        "evals_form": evals_form,
        "process_name": process_name,
    })
