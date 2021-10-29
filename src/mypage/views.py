from django.shortcuts import render, redirect
from users.models import Places, Favo, Evals
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Q, Avg


# class MypageView(generic.TemplateView):
#     template_name = 'mypage/mypage.html'

def MypageView(request):
    evals = Evals.objects.all()
    user = request.user
    # favo_table = Favo.objects.filter(favo_usr_id=user).all()
    place_id_list = Favo.objects.values("favo_place_id").filter(favo_usr_id=user)
    place_evals = Evals.objects.all().values('place_id_id').annotate(avg_silence=Avg('silence')).annotate(avg_concentrations=Avg('concentrations')).annotate(avg_cost_pafo=Avg('cost_pafo')).annotate(avg_conges=Avg('conges'))
    print(place_id_list)
    places =[]
    for favo_place in place_id_list.values():
        places.append(Places.objects.get(pk=favo_place['favo_place_id_id']))
    print(places)
    return render(request, "mypage/mypage.html", {
        'places': places, 'evals': place_evals,
    })

    
    
    
    
    
    # print("id_list={}".format(place_id_list))
    # favorite_places = []
    # for place_id in place_id_list:
    #     favorite_places = Places.objects.filter(place_id=place_id)
        # favorite_places.append(Places.objects.filter(place_id=place_id)) 

    # print(favorite_places)
    

    # return render(request, 'mypage/mypage.html', {
    #     'test': test
    # })



# def show_favorite(self, request):
#     user_id= self.request.user
#     # favo_place_id = Favo.objects.filter(user_id=user_id).all()
#     favo_place_id = user_id.favo_set.all()
#     print(favo_place_id)
#     #　favoにあるplace_idからplaceをとる
#     favorite_places = Places.objects.filter(place_id=favo_place_id).all()
    
#     return render(request, "users/my_page.html", {
#         'favorite_places':favorite_places
#     })