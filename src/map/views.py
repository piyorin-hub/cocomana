from django.shortcuts import render
from django.views import generic
import googlemaps
from django.db.models import Sum
from users.models import Places, Evals

# Create your views here.
# class TopView(generic.TemplateView):
#     template_name = 'map/home.html'

def images(request):
    return render(request, 'map/test.html')

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
        evals ={"concentrations":0, "silence":0, "cost_pafo":0, "conges":0}
        count = Evals.objects.filter(place_id = obj.pk).count()
        obj_1 = Evals.objects.filter(place_id = obj.pk).aggregate(concentrations = Sum('concentrations'))
        obj_2 = Evals.objects.filter(place_id = obj.pk).aggregate(silence = Sum('silence'))
        obj_3 = Evals.objects.filter(place_id = obj.pk).aggregate(cost_pafo = Sum('cost_pafo'))
        obj_4 = Evals.objects.filter(place_id = obj.pk).aggregate(conges = Sum('conges'))
        evals["concentrations"] = obj_1["concentrations"] / count
        evals["silence"] = obj_2["silence"] / count
        evals["cost_pafo"] = obj_3["cost_pafo"] / count
        evals["conges"] = obj_4["conges"] / count
        strong = max(evals, key=evals.get)
        # print(strong)
        # print(evals[strong])
        loc ={'id':obj.pk, "name":obj.place_name , 'lat':adress_dic[0]["geometry"]["location"]["lat"], 'lng':adress_dic[0]["geometry"]["location"]["lng"], 'adress':adress, 'strong':strong, 'para':evals[strong]}
        results.append(loc)
        
        #place_results = gmaps.places_nearby(location=loc, radius=1000, keyword='',language='ja') #半径1000m以内のカフェ情報を取得
    return render(request, 'map/home.html', {
        "searchAdress":searchAdress,
        "data": results,
    })