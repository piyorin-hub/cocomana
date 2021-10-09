from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from .forms import LoginForm, SignupForm, UserUpdateForm , MyPasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model 
from django.contrib.auth.mixins import UserPassesTestMixin 
from django.contrib.auth.models import User
from django.urls import reverse_lazy # 遅延評価用
from users.models import Places, Favo

'''ログイン'''
class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


'''ログアウト'''
class Logout(LogoutView):
    template_name = 'users/logout_done.html'


'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']


'''マイページ'''
class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'users/my_page.html'

    def my_page(request):
        spaces = Places.objects.first()
        return render(request, 'users/my_page.html', {
            'spaces': spaces
        })

    # def my_page(self, request):
    #     user_id= self.request.user
    #     favo_place_id = Favo.objects.filter(user_id=user_id).all()
    #     print(favo_place_id)
    #     #　favoにあるplace_idからplaceをとる
    #     favorite_places = Places.objects.filter(place_id=favo_place_id).all()
        
    #     return render(request, "users/my_page.html", {
    #         'favorite_places':favorite_places
    #     })



'''サインアップ'''
class Signup(generic.CreateView):
    template_name = 'users/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('users:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    template_name = 'users/signup_done.html'


'''ユーザー登録情報の更新'''
class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return resolve_url('users:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

'''パスワード変更'''
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


'''パスワード変更完了'''
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'



