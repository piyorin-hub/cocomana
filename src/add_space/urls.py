from django.urls import path, include
from . import views


app_name ='add_space'

urlpatterns = [
    path("", views.add_space, name="add_space")
]