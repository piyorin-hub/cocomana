from django.shortcuts import render
from django.views import generic
import googlemaps
from users.models import Places

# Create your views here.
# class TopView(generic.TemplateView):
#     template_name = 'map/home.html'

def returnGeocode(request):
    queries = request.POST.get('q')
    googleapikey = 'AIzaSyCmy9n811gkYviPHi50c7KnsFQb_Cc7Al4'
    gmaps = googlemaps.Client(key=googleapikey)
    searchAdress = {'None':0}
    if queries:
        adress_dic = gmaps.geocode(queries)
        searchAdress =  {'lat':adress_dic[0]["geometry"]["location"]["lat"], 'lng':adress_dic[0]["geometry"]["location"]["lng"]}
    #else:
    places = Places.objects.all()
    results = []
    for obj in places:
        #print(obj.place_name)
        adress = obj.prefecture + " " + obj.municipal + " " + obj.place_address
        adress_dic = gmaps.geocode(adress)
        loc ={'id':obj.pk, "name":obj.place_name , 'lat':adress_dic[0]["geometry"]["location"]["lat"], 'lng':adress_dic[0]["geometry"]["location"]["lng"], 'place_name':obj.place_name}
        results.append(loc)

        #place_results = gmaps.places_nearby(location=loc, radius=1000, keyword='',language='ja') #半径1000m以内のカフェ情報を取得
    return render(request, 'map/home.html', {
        "searchAdress":searchAdress,
        "data": results,
    })