'''
https://www.acmicpc.net/problem/11399
'''
import sys
input = sys.stdin.readline
num = int(input())
persons = [int(x) for x in input().split()].sort()
time = total_time = 0
for person in persons:
    time += person
    total_time += time
print(total_time)
