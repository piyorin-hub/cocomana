from django.urls import path, include
from . import views


app_name ='mypage'

urlpatterns = [
    path('', views.MypageView, name='mypage')
]