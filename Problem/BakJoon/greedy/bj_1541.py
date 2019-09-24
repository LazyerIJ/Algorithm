'''
https://www.acmicpc.net/problem/1541
number can start with '0' << use regex
'''
import sys
import re
input = sys.stdin.readline

num = input()[:-1]
num = [x for x in re.split('(\d+)', num) if x]
flag = False
for i, n in enumerate(num):
    if n == '-':
        flag = True
    elif n == '+' and flag:
        num[i] = '-'
    elif n.isdigit():
        num[i] = str(int(n))
print(eval(''.join(num)))
