'''
https://www.acmicpc.net/problem/1697
0<=N<=100,000
0<=M<=100,000
N -> +1, -1 *2: find M
'''
import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
VISITED = [False] * 100001
EDGES = deque()
EDGES.append([N, 0])
rs = None

while True:
    cur_position, rs = EDGES.popleft()
    if cur_position == M:
        break
    next_position = [cur_position+1, cur_position-1, cur_position*2]
    for position in next_position:
        if position<0 or position>100000:
            continue
        if not VISITED[position]:
            VISITED[position] = True
            EDGES.append([position, rs+1])
print(rs)









