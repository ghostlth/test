from django.shortcuts import render
from .testmail import send
from django.http import HttpResponse
from .changePwd import changePwd

def sendmail(request):
    return render(request,'sendmail.html')

def show_result(request):
    user = request.GET.get('user',None)
    user = str(user)+'@szhq.com'
    result = send(user)
    if result[0]=='发送成功':
        code = result[1]
        print(code)
    ret = result
    return HttpResponse(ret)

def change_pwd(request):
    userid = request.GET.get('userid',None)
    userid = userid + '@szhq.com'
    changePwd(userid)
    return HttpResponse(userid)