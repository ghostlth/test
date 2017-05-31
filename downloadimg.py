import requests
import http.cookiejar
import re,os,time,random

'''
测试
'''

agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {
    'Host':'www.24meinv.me',
    'Origin':'http://www.24meinv.me',
    'Referer':'http://www.24meinv.me/login.aspx',
    'Upgrade-Insecure-Requests':'1',
    'Connection':'keep-alive',
    'User-Agent':agent
}

session = requests.session()
session.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
# 加载cookies
try:
    session.cookies.load(ignore_discard = True)
except:
    print('cookies未加载')
# 获取登录所需信息
def get_data():
    index_url = 'http://www.24meinv.me/login.aspx'
    index_page = session.get(index_url,headers=headers)
    html = index_page.text
    pattern = r'id="__VIEWSTATE" value="(.*?)".*?id="__VIEWSTATEGENERATOR" value="(.*?)"'
    result = re.findall(pattern,html,re.S)
    return result[0]
# 判断是否登陆
def islogin():
    url = 'http://www.24meinv.me/member/medit.aspx'
    login_code = session.get(url,headers=headers,allow_redirects = False).status_code
    if login_code == 200:
        return True
    else:
        return False
#登陆
def login():
    result = get_data()
    __VIEWSTATE = result[0]
    __VIEWSTATEGENERATOR = result[1]
    headers['X-Requested-With'] = 'XMLHttpRequest'
    post_url = 'http://www.24meinv.me/login.aspx'
    postdata = {
        'TextBox1':'gghhoosstt',
        'TextBox2':'1qaz2wsx',
        '__VIEWSTATE':__VIEWSTATE,
        '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
        'Button1':'马上登录'
    }
    session.post(post_url,data=postdata,headers=headers)
    session.cookies.save()

def get_index():
    url = 'http://www.24meinv.me/gaoqing/beauty_1.html'
    index_page = session.get(url,headers=headers)
    html = index_page.text
    pattern = r'<li><a href=".*?".*?alt=".*? (.*?)"'
    index = re.findall(pattern,html,re.S)
    return index

def get_ip_list():
    f = open(r'C:\Users\Administrator\Desktop\新建文件夹\Practice\proxies.txt','r')
    c = f.readlines()
    proxys = []
    for i in c :
        ip = i.strip('\n').split(' ')
        proxy_host = 'http://'+ ip[0]+ ip[1]
        proxy_temp = {'http':proxy_host}
        proxys.append(proxy_temp)
    return proxys

def get_random_proxy():
    url = 'http://ip.chinaz.com/getip.aspx'
    proxy_list = get_ip_list()
    proxies = random.choice(proxy_list)
    try:
        respone = session.get(url,proxies=proxies).text
        print(respone)
    except:
        get_random_proxy()
    return proxies

def get_img(host):
    index = get_index()
    for i in index:
        downindex = 'F:/img/%s'%i
        if os.path.exists(downindex) ==False:
            os.mkdir(downindex)
        for j in range(0,60):
            n = '%02d'%j
            url = 'http://img.diercun.com/hd/Beautyleg/%s/00%s.jpg'%(i,n)
            print(url)
            filepath = downindex + '/' + n + '.jpg'
            if os.path.exists(filepath):
                print('跳过')
                continue
            else:
                headers = {
                    'Accept':'image/webp,image/*,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate, sdch',
                    'Accept-Language':'zh-CN,zh;q=0.8',
                    'Connection':'keep-alive',
                    'Host':'img.diercun.com',
                    'Referer':'http://www.24meinv.me/2014/1-28/tuimo14525_5.html',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                }
                proxies = {
                    'http':host
                }
                downing = session.get(url,headers=headers,proxies=proxies)
                status = downing.status_code
                c = downing.content
                if status == 200:
                     try:
                         with open(filepath,'wb') as f:
                            f.write(c)
                            f.close()
                     except Exception as e:
                         print(e)
                         continue
                time.sleep(2)



host = 'http://139.224.237.33:8888'
login()
print(islogin())
get_img(host)

# get_random_proxy()
# print(get_index())