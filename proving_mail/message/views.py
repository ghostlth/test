from django.shortcuts import render
from .testmail import send

def sendmail(request):
    return render(request,'sendmail.html')

def show_result(request):
    user = request.GET.get('user',None)
    user = str(user)+'@szhq.com'
    return send(request,user)