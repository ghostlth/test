import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from django.http import HttpResponse

def get_code():
    codes = []
    for i in range(0-9):
        codes.append(str(i))
    for i in range(65,91):
        codes.append(chr(i))
    for i in range(97,123):
        codes.append(chr(i))
    my_code =random.sample(codes,6)
    ver_code = ''.join(my_code)
    return ver_code

def send(request,user):
    mail_host = 'mail.szhq.com'
    mail_user = 'lthui@szhq.com'
    mail_pass = '1qaz@WSX?'
    mes = get_code()

    sender = 'lthui@szhq.com'
    receivers = [user]

    message = MIMEText(mes, 'html', 'utf-8')
    message['From'] = Header('test', 'utf-8')
    message['To'] = Header('冰是沉默的水', 'utf-8')
    message['Subject'] = Header('test', 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('发送成功')
        return HttpResponse('发送成功')
    except smtplib.SMTPException:
        print('发送失败')
        return HttpResponse('发送失败')

