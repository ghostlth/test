#coding:utf-8
import requests
import time
# import random,base64,string


def login():
    session = requests.session()
    loginUrl = 'https://passport.weibo.cn/sso/login'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'passport.weibo.cn',
        'Origin': 'https://passport.weibo.cn',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    data = {
        'username': '******',
        'password': '******',
        'savestate': 1,
        'r': 'https://m.weibo.cn/',
        'ec': '0',
        'pagerefer': 'https://m.weibo.cn/',
        'entry': 'mweibo',
        'mainpageflag': '1'
    }
    rep = session.post(loginUrl,data,headers=headers)
    # print(rep.content)
    return session


def getSt(session):
    stHeaders = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'X-DevTools-Emulate-Network-Conditions-Client-Id': 'ECAB82F3906D1F7216C0199BFD3B613D'
    }
    stUrl = 'https://m.weibo.cn/api/config'
    res = session.get(stUrl,headers=stHeaders).json()
    st = res['data']['st']
    print(st)
    return st

def upload(session,content):
    uploadUrl = 'https://m.weibo.cn/api/statuses/update'
    headers = {
        'Accept': 'application/json, text/plain,*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',

        'Origin': 'https://m.weibo.cn',
        'Referer': 'https://m.weibo.cn/compose/index?pwa=1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'X - Requested - With': 'XMLHttpRequest'
    }

    st = getSt(session)
    # data = {
    #     'type':'json',
    #     'pic':file,
    #     'st':st
    #
    # }
    data = {
        'content': content,
        'st': st
    }
    try:
        res = session.post(uploadUrl,data,headers=headers)
        # print(res.content)
        print('发送成功')
    except Exception as e:
        print('false:'+str(e))


# def uploadPic(session):
#
#     headers = {
#         'Accept': 'application / json, text / plain, * / *',
#         'Accept - Encoding': 'gzip, deflate, br',
#         'Accept - Language': 'zh - CN, zh;q = 0.9',
#         'Connection': 'keep - alive',
#
#         'Host': 'm.weibo.cn',
#         'Origin': 'https: // m.weibo.cn',
#         'Referer': 'https: // m.weibo.cn / compose',
#         'User - Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
#         'X - Requested - With': 'XMLHttpRequest'
#     }
#
#     picUrl = 'https://m.weibo.cn/api/statuses/uploadPic'
#
#     st = getSt(session)
#     files = {
#         'type': 'json',
#         'pic': open(r'C:\Users\dell\Desktop\utils\Demo\source\Koala.jpg', 'rb'),
#         'st': st
#     }
#
#     boundary = ''.join(random.sample(string.ascii_letters + string.digits, 16))
#     print(boundary)
#
#     headers['Content-Type'] = 'multipart/form-data;boundary=----WebKitFormBoundary' + boundary
#     pic = session.post(picUrl, files, headers=headers)
#     print(pic.json())

def spider():

    return

def sendWeibo():
    session = login()
    content = '晚安'
    upload(session,content)


if __name__ == '__main__':
    sendWeibo()