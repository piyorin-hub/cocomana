from django.urls import path
from . import views


app_name ='map'

urlpatterns = [
    # path('', views.TopView.as_view(), name='home'),
    path("images/", views.images, name="images"),
    path('', views.returnGeocode, name="home"),
]