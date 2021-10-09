from django.urls import path
from . import views


app_name ='space'

urlpatterns = [
    path('space/<int:placeid>/', views.index, name="index"),
    path("add_review",views.generateView,name="add_review")
]