#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
from  bs4 import BeautifulSoup

start_url = 'http://www.cambricon.com/zhaoxiannashi/'  # 起始网页

# 模拟浏览器登陆
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
# 解析爬取的网址
start_html = requests.get(start_url, headers=headers)
start_html.encoding = start_html.apparent_encoding
soup = BeautifulSoup(start_html.text, 'lxml')

# print(soup.prettify())
list_page = soup.find('div', class_='coll').find_all('a')
for i in list_page:
    hrefs = i['href']
    link = 'http://www.cambricon.com' + hrefs
    # print(link)  # 获取所有的招聘入口
    url_job = requests.get(link, headers=headers)
    url_job.encoding = url_job.apparent_encoding
    soup_job = BeautifulSoup(url_job.text, 'lxml')
    content = soup_job.find('div', class_='collb_lb').find_all('p')
    for k in content:
        txt = k.get_text()
        with open('job.txt', encoding='utf-8', mode='a+') as  f:
            f.write('\r\n')
            f.write(txt + '\r\n')
        print(k.get_text())
