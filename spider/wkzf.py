# coding=utf-8
import re
import requests
from  bs4 import BeautifulSoup

all_url = 'https://www.wkzf.com/shanghai/esf/d1-p1'
# 模拟浏览器登陆
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

start_html = requests.get(all_url, headers=headers)  # 传入起始网址  headers
start_html.encoding = start_html.apparent_encoding  # 网页编码  自适应
soup = BeautifulSoup(start_html.text, 'lxml')
list_page = soup.find('a', class_='esf_Model WKBigDataBtn')
content = {'name': '',
           'price': '',
           'model': '',
           'size': '',
           'build_time': '',
           'subway': '',
           'school': '',
           'address': ''}
name = soup.find('p', class_='fz16 htitle').get_text()
content['name'] = name
price = soup.find('p', class_='moneynum').get_text()
content['price'] = price
model = soup.find('p', class_='fz14 yearbox').find_all('span')[0].get_text()
content['model'] = model
size = soup.find('p', class_='fz14 yearbox').find_all('span')[1].get_text()
content['size'] = size
build_time = size = soup.find('p', class_='fz14 yearbox').find_all('span')[2].get_text()
content['build_time'] = build_time
subway = soup.find('p', class_='fz14 yearbox').find_all('span')[3].get_text()
content['subway'] = subway
school = soup.find('p', class_='address').get_text()
content['school'] = school
address = soup.find_all('p', class_='address')[1].get_text()
content['address'] = address
