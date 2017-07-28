from selenium import webdriver
import time
import json


driver = webdriver.Chrome()

def changePwd(userid):
    url1 = 'http://172.88.13.6/login/Login.jsp?logintype=1'
    driver.get(url1)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginid"]').send_keys('sysadmin')
    driver.find_element_by_xpath('//*[@id="userpassword"]').send_keys('Hq2017')
    driver.find_element_by_xpath('//*[@id="login"]').click()
    time.sleep(3)
    url2 = 'http://172.88.13.6/hrm/search/HrmResourceSearch.jsp?_fromURL=HrmResourceSearch&fromHrmTab=1'
    driver.get(url2)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="advancedSearchDiv"]/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/input').send_keys()

def getUserID(userid):
    url_sql = 'http://172.88.13.6/sQLRunner.c'
    driver.get(url_sql)


# changePwd()
