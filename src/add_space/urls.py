from django.urls import path, include
from . import views


app_name ='add_space'

urlpatterns = [
    path("", views.generateView, name="add_space")
]