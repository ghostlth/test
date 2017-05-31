import requests
import socket


def get_proxy_host():
    f = open(r'C:\Users\Administrator\Desktop\新建文件夹\Practice\proxies.txt','r')
    l = f.readlines()
    f.close()
    host_list = []
    for i in l :
        i = 'http://'+i.strip('\n')
        host_list.append(i)
    return host_list

socket.setdefaulttimeout(3)
url = 'http://ip.chinaz.com/getip.aspx'
host_list = get_proxy_host()
useful_ip = []

for host in host_list:
    proxy = {
        'http':host
    }
    try:
        res = requests.get(url,proxies=proxy).text
        r = res.encode('utf-8')
        useful_ip.append(host)
        print(res)
    except Exception as e:
        print(e)
        continue
f = open(r'C:\Users\Administrator\Desktop\新建文件夹\Practice\ip_list.txt','w')
for i in useful_ip:
    f.write(i+'\n')
f.close()

