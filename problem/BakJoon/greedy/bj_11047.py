'''
https://www.acmicpc.net/problem/11047
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
cnt = 0
for _ in range(N):
    coins.insert(0, int(input()))
for coin in coins:
    tmp = K//coin
    cnt += tmp
    K -= tmp*coin
print(cnt)


