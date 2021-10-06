from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import Places, Evals


class SaveForm(forms.ModelForm):

    class Meta:
        model = Places
        fields = ('place_name', 'open_time', 'close_time','prefecture','municipal','place_address', 'wifi', 'charge', 'personal_space', 'place_cost', 'place_category')
        labels = {
            'place_name':"スペースの名前",
            'open_time':"営業開始時間",
            'close_time':"閉店時間",
            'prefecture' : "都道府県",
            'municipal': "市区町村",
            'place_address': "番地と建物名",
            'wifi':"wifiの有無",
            'charge':"コンセントの有無",
            'personal_space':"個室の有無",
            'place_cost':"コーヒー一杯の値段",
            'place_category':"スペースの種類"
        }

class EvalsForm(forms.ModelForm):
    class Meta:
        model = Evals
        fields = ('concentrations', 'silence', 'cost_pafo', 'conges')
        labels = {
            'concentrations':"集中度",
            'silence':"静かさ",
            'cost_pafo':"コストパフォーマンス",
            'conges' : "空いている度",
        }
        exclude = ('place_id',)