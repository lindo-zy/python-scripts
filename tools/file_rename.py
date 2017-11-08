# 批量修改文件名
'''
原文文件名为 chapter1.py，chapter2.py.....chapter19.py
修改文件名为 chapter01.py,chapter02.py.....chapter19.py

'''

import os, re

f = os.listdir(os.getcwd())
# print(f)
for i in f:
    pattern = re.compile(r'chapter\d{0,2}')
    match = re.search(pattern, i)
    if match:
        filename = match.group()
        num = int((re.sub(r'.*[^0-9]', '', filename)))
        m = 'chapter' + '%02d' % num + '.py'
        print(m, filename)
        os.rename(filename + '.py', m)
