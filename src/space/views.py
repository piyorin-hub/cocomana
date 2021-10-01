from django.shortcuts import render
from django.http import HttpResponse

from users.models import Places, Evals

def space(request, p_id):
    if request.method == 'POST':
        space = Places.objects.get(place_id = p_id)
        evals = Evals.objects.get(place_id = p_id)
        return render(request,"space/index.html",{
            'space':space,'evlas':evals})
