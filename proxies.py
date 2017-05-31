import requests
import re

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
session = requests.session()
url = 'http://www.xicidaili.com/nn/1'
req = session.get(url,headers=header)
res = req.text
pattern = r'class="odd.*?<td>(.*?)</td>.*?<td>(.*?)</td>'
c = re.findall(pattern,res,re.S)
f= open(r'C:\Users\Administrator\Desktop\新建文件夹\Practice\proxies.txt','w')
for i in c:
    print(i)
    s = i[0]+':'+i[1]
    f.write(s+'\n')
f.close()
