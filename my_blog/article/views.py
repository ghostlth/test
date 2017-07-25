from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,my_args):
    post = Article.objects.get(id=int(my_args))
    return render(request,'detail.html',{'post':post})