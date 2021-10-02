from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Places, Evals
from django.views import generic
from .forms import SaveForm

# Create your views here.
# class SaveSpace(generic.CreateView):
#     template_name = 'add_space/add_space.html'
#     form_class =SaveForm

#     #GET時の処理を記載
#     def get(self,request):
#         context = {}
#         context["process_name"] = "スペースの追加"
#         return render(request, "add_space/add_space.html",context)

#     #POST時の処理を記載
#     def post(self,request):
#         if request.method == "POST":
#             form = SaveForm.Contact_Form(request.POST)
            
#             #フォーム入力が有効な場合
#             if form.is_valid():
#                 #入力項目をデータベースに保存
#                 form.save(commit=True)

#         return render(request, "users/top.html")

class SaveSpace(generic.CreateView):
    template_name = 'add_space/add_space.html'
    form_class =SaveForm

    def form_valid(self, form):
        places = form.save() # formの情報を保存
        return redirect('users:top')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "スペースの追加"
        return context
