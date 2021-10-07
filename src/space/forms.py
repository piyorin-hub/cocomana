from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import Reviews


class SaveForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('review_place_id','review_user_id','review_comment')
        labels = {
            'review_place_id':"スペースのid",
            'review_user_id':"ユーザーのid",
            'review_comment':"レビューのコメント",
        }