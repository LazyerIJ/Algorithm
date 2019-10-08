'''
https://www.acmicpc.net/problem/1629
'''
A, B, C = map(int, input().split(' '))

def split_and_mutiply(a, b, c):
    if b == 1:
        return a % c
    elif b%2 == 0:
        return pow(split_and_mutiply(a, b//2, c), 2) % c
    elif b%2 == 1:
        return a * pow(split_and_mutiply(a, b//2, c), 2) % c

print(split_and_mutiply(A, B, C))

