from django.urls import path
from . import views


app_name ='space'

urlpatterns = [
    path('space/<int:placeid>/', views.index, name="index"),
    path("add_review/<int:placeid>",views.review,name="add_review"),
    path("add_evaluation/<int:placeid>",views.evaluation,name="add_evaluation"),
    path("<int:pk>", views.favorite, name="favorite")
]