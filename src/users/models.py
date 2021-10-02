from config.settings import TIME_ZONE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Places(models.Model): #ok
    place_id = models.IntegerField(primary_key=True)
    place_name = models.TextField(max_length=50)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    place_address = models.TextField(max_length=100)
    wifi = models.BooleanField()
    charge = models.BooleanField()
    personal_space = models.BooleanField()
    place_cost = models.PositiveIntegerField(null=True, blank=True)
    place_category = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #1:cafe, 2:コワーキングスペース, 3:food(マックとか), 4:図書館, 5:その他

class Evals(models.Model):#ok
    evals_id = models.IntegerField(primary_key=True)
    place_id = models.ForeignKey(Places, on_delete=models.CASCADE) #外部キー
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #外部キー
    concentrations = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #最大値５
    silence = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cost_pafo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    conges = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Favo(models.Model): #ok
    favo_id = models.IntegerField(primary_key=True)
    favo_usr_id = models.ForeignKey(User, on_delete=models.CASCADE)
    favo_place_id = models.ForeignKey(Places, on_delete=models.CASCADE)

class Reviews(models.Model): #ok
    reviews_id = models.IntegerField(primary_key=True)
    review_comment = models.TextField(max_length=150) #文字数制限するか
    review_date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    review_place_id = models.ForeignKey(Places, on_delete=models.CASCADE)
    review_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
