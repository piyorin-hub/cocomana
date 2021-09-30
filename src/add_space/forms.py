from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import Places


class SaveForm(forms.ModelForm):

    class Meta:
        model = Places
        fields = ('place_name', 'open_time', 'close_time','place_address', 'wifi', 'charge', 'personal_space', 'place_cost', 'place_category')
        labels = {
            'place_name':"スペースの名前",
            'open_time':"営業開始時間",
            'close_time':"閉店時間",
            'place_address':"お店の住所",
            'wifi':"wifiの有無",
            'charge':"コンセントの有無",
            'personal_space':"個室の有無",
            'place_cost':"コーヒー一杯の値段",
            'place_category':"スペースの種類"
        }
