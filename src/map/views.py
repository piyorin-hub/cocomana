from django.shortcuts import render
from django.views import generic
import googlemaps
from users.models import Places

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'map/home.html'

def returnGeocode(request):
    #今回入力された住所から近くを取り出してそのリストを渡す
    queries = request.POST.get('q')
    googleapikey = 'AIzaSyCmy9n811gkYviPHi50c7KnsFQb_Cc7Al4'
    gmaps = googlemaps.Client(key=googleapikey)
    now_adress = {}
    if queries:
        adress_dic = gmaps.geocode(queries)
        now_adress =  {'lat':adress_dic[0]["geometry"]["location"]["lat"], 'lng':adress_dic[0]["geometry"]["location"]["lng"]}
    #else:
    places = Places.objects.all()
    results = []
    for obj in places:
        print(obj.place_name)
        adress = obj.prefecture + " " + obj.municipal + " " + obj.place_address
        adress_dic = gmaps.geocode(adress)
        loc ={'id':obj.pk, 'lat':adress_dic[0]["geometry"]["location"]["lat"], 'lng':adress_dic[0]["geometry"]["location"]["lng"], 'place_name':obj.place_name}
        results.append(loc)


        #place_results = gmaps.places_nearby(location=loc, radius=1000, keyword='',language='ja') #半径1000m以内のカフェ情報を取得

    return render(request, 'map/test.html', {
        "now_adress":now_adress,
        "results": results,
    })

# from users.models import Places, Evals
# from django.db.models import Q

# def index(request):
#     #
#      queries = request.GET.get('q')
#      evals = Evals.objects.all()
#      if queries:
#          if " " in queries or "　" in queries:
#              queries = queries.split()
#              for query in queries:
#                 places = Places.objects.all().order_by()
#                 places.append = places.filter(
#                     Q(place_name__icontains=query)|
#                     Q(wifi__icontains=query)|
#                     Q(personal_space__icontains=query)|
#                     Q(prefecture__icontains=query)|
#                     Q(municipal__icontains=query)|
#                     Q(place_address__icontains=query)
#                     ).distinct()
             
#          else:
#              query = queries
#              print(query)
#              places = Places.objects.all().order_by()
#              places = places.filter(
#                  Q(place_name__icontains=query)|
#                  Q(wifi__icontains=query)|
#                  Q(personal_space__icontains=query)|
#                  Q(prefecture__icontains=query)|
#                  Q(municipal__icontains=query)|
#                  Q(place_address__icontains=query)
#                  ).distinct()

#      else:
#          query = queries
#          places = Places.objects.all().order_by()
#      place_id = Places.objects.values('place_id')
#      print(Places.objects.values('place_id'))
          
#      return render(request, "search/index.html", {
#          'places': places, 'query': query,
#          'evals': evals
#      })