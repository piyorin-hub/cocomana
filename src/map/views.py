from django.shortcuts import render
from django.views import generic
import googlemaps
from users.models import Places

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'map/home.html'

def returnGeocode(request):
    #今回入力された住所から近くを取り出してそのリストを渡す
    googleapikey = 'AIzaSyCmy9n811gkYviPHi50c7KnsFQb_Cc7Al4'
    gmaps = googlemaps.Client(key=googleapikey)
    places = Places.objects.all()
    
    result = gmaps.geocode("東京都 武蔵野市 吉祥寺 本町")
    loc ={'lat':result[0]["geometry"]["location"]["lat"], 'lng':result[0]["geometry"]["location"]["lng"]}

    #place_results = gmaps.places_nearby(location=loc, radius=1000, keyword='',language='ja') #半径1000m以内のカフェ情報を取得
    print(result)

    return render(request, 'map/geocode_test.html', {
        "result": result,
    })


from users.models import Places, Evals
from django.db.models import Q

def index(request):
    #
     queries = request.GET.get('q')
     evals = Evals.objects.all()
     if queries:
         if " " in queries or "　" in queries:
             queries = queries.split()
             for query in queries:
                places = Places.objects.all().order_by()
                places.append = places.filter(
                    Q(place_name__icontains=query)|
                    Q(wifi__icontains=query)|
                    Q(personal_space__icontains=query)|
                    Q(prefecture__icontains=query)|
                    Q(municipal__icontains=query)|
                    Q(place_address__icontains=query)
                    ).distinct()
             
         else:
             query = queries
             print(query)
             places = Places.objects.all().order_by()
             places = places.filter(
                 Q(place_name__icontains=query)|
                 Q(wifi__icontains=query)|
                 Q(personal_space__icontains=query)|
                 Q(prefecture__icontains=query)|
                 Q(municipal__icontains=query)|
                 Q(place_address__icontains=query)
                 ).distinct()

     else:
         query = queries
         places = Places.objects.all().order_by()
     place_id = Places.objects.values('place_id')
     print(Places.objects.values('place_id'))
          
     return render(request, "search/index.html", {
         'places': places, 'query': query,
         'evals': evals
     })