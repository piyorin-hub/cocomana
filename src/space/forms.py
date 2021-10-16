from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import Reviews, Evals


class SaveForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('review_comment',)
        labels = {
            'review_comment':"レビュー",
        }
        
        exclude = ('review_place_id',)

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