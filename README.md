# python-scripts
一些遇到的python题
***
1.用户输入一句话，求出里面数字的和，如 ‘i am 12 years old,i am grade 6’，输出18
```python
s = 'i am 12 years old,i am grade 6'
l = s.split(' ')
sum = 0
for i in l:
    if i.isdigit():
        sum += int(i)
print(sum)
```
2.设有n个正整数，将他们连接成一排，组成一个最大的多位整数。  
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。  
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。  
```python
from functools import cmp_to_key
num = input('输入n：')
l = input('输入n个数，空格分隔').split(' ')
l.sort(key=cmp_to_key(lambda a, b: (int(a + b) > int(b + a)) - (int(a + b) < int(b + a))), reverse=True)
print(''.join(l))
```
---
3.给定一个十进制的正整数number，选择从里面去掉一部分数字，希望保留下来的数字组成的正整数最大。  
如n为325，m为1，结果为35
```python
num = list(input('请输入一个整数：'))
cnt = int(input('输入删除个数:'))
for i in range(cnt):
    num.remove(min(num))
print(''.join(num))

```
4. 字符串首尾相连，里面必须包含ABCDE  
输入：
ABCYDYE   
ATTMBQECPD  
输出:  
1  
3
```python



```
5. “水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数
```python
start, end = input("输入范围：").split()
sum = 0
for num in range(int(start), int(end)):
    n = len(str(num))
    for i in str(num):
        sum += int(i) ** n
    if num == sum:
        print(num)
    sum = 0



```
6.给定一个英文字符串,请写一段代码找出这个字符串中首先出现三次的那个英文字符。如:输入Have you ever gone shopping and，输出e  
```python
str =input("输入字符串:")
for i in range(len(str)):
    s=str[i]
    if s.isalpha():
        num = str[0:i + 1].count(s)
        if num == 3:
            print(s)
            break





```
7.按照6+8+4打印出身份证
```python

s = input().replace(' ', '')
if len(s) <= 6:
    print(s)
elif len(s) <= 14:
    print(s[0:6], s[6:])
else:
    print(s[0:6], s[6:14], s[14:])
```