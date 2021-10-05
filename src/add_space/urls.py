from django.urls import path, include
from . import views


app_name ='add_space'

urlpatterns = [
    #path("", views.SaveSpace.as_view(), name="add_space")
    path("", views.generateView, name="add_space")
]