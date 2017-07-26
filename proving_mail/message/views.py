from django.shortcuts import render
from .testmail import send
from django.http import HttpResponse

def sendmail(request):
    return render(request,'sendmail.html')

def show_result(request):
    user = request.GET.get('user',None)
    user = str(user)+'@szhq.com'
    result = send(user)
    if result[0]=='发送成功':
        code = result[1]
        print(code)
    ret = result[0]

    return HttpResponse(ret)
