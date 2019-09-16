'''
https://www.acmicpc.net/problem/2217
'''
import sys
input = sys.stdin.readline
num = int(input())
ropes = []
for _ in range(num):
    ropes.append(int(input()))
ropes.sort(reverse=True)
part_sum = 10001
rs = []
for i, rope in enumerate(ropes):
    part_sum = min(part_sum, rope)
    rs.append(part_sum * (i+1))
print(max(rs))
