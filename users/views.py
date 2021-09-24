from django.shortcuts import render
from django.views import generic


'''トップページ'''
class TempView(generic.TemplateView):
    template_name = 'account/top.html'

