from django.urls import path
from . import views


app_name ='search'

urlpatterns = [
    path("", views.index, name="index"),
    # path('space/<int:place_id>/', views.index, name="index")
]