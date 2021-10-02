from django.urls import path
from . import views


app_name ='space'

urlpatterns = [
    path("", views.space, name="index")
]