from django.urls import path
from . import views


app_name ='map'

urlpatterns = [
    # path('', views.TopView.as_view(), name='home'),
    path('', views.returnGeocode, name="home"),
]