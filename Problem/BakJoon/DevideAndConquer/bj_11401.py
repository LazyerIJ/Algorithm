'''
https://www.acmicpc.net/problem/11401
- 이항계수
- 페르마의 소정리
- 곱셈의 역원
'''

MAXIMUM = 1000000007
N, K = map(int, input().split(' '))

def pow(a, b):
    rs = 1
    aa = a
    while (b > 0):
        if b%2 == 1:
            rs = rs * aa % MAXIMUM
        b = b//2
        aa = (aa*aa) % MAXIMUM
    return rs

def fac(s, e):
    val = 1
    for i in range(s, e+1):
        val = (val*i) % MAXIMUM
    return val

def calc_binomial_coefficient(n, k):
    val1 = fac(1, n-k)
    val3 = fac(k+1, n)
    return val3%MAXIMUM * pow(val1,MAXIMUM-2) % MAXIMUM

print(calc_binomial_coefficient(N, K))

