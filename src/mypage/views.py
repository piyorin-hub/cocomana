from django.shortcuts import render, redirect
from users.models import Places, Favo
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User


# class MypageView(generic.TemplateView):
#     template_name = 'mypage/mypage.html'

def MypageView(request):
    # test = Places.objects.first()
    user_id= request.user
    # favo_place_id = Favo.objects.filter(user_id=user_id).all()
    favo_place_id = user_id.favo_set.all()
    print(favo_place_id)
    #　favoにあるplace_idからplaceをとる
    favorite_places = Places.objects.filter(place_id=favo_place_id).all()
    
    return render(request, "mypage/mypage.html", {
        'favorite_places':favorite_places
    })

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