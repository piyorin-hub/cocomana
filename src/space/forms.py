from django import forms
#モデルクラスを呼出
from users.models import Reviews

#フォームクラス作成
class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Reviews

        #②表示するモデルクラスのフィールドを定義
        fields = ('review_user_id','review_comment')

        #③表示ラベルを定義
        labels = {'review_user_id':"id",
                  'review_comment':"コメント",
        }
