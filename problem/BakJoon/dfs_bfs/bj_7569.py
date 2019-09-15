'''
https://www.acmicpc.net/problem/7569
자꾸 시간초과 떠서 고생...

if (not VISITED[z][h][x]) and (GRAPH[z][h][x] ==0) --> timeout
if GRAPH[z][h][x]==0 --> SUCCESS

list -> list.pop(0) -> timeout
collections.deque -> deque.popleft() -> SUCCESS
queue.deque -> queue.popleft() -> SUCCESS
'''
import sys
#from collections import deque
from queue import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

directions = [[0, 0, 1], [0, 0, -1],
              [0, 1, 0], [0, -1, 0],
              [-1, 0, 0], [1, 0, 0]]

WIDTH, DIM, HEIGHT = map(int, input().split()) 
GRAPH = []
edges = deque()
RS = 0
tomatos = 0
cnt = 0
for i in range(HEIGHT):
    floor = []
    for j in range(DIM):
        tmp = list(map(int, input().split()))
        for k,t in enumerate(tmp):
            if t == 0:
                tomatos += 1
            elif t == 1:
                edges.append([k,j,i,0])
        floor.append(tmp)
    GRAPH.append(floor)

while edges:
    x, y, z, RS = edges.popleft()
    #x, y, z, RS = edges.pop(0)
    for direction in directions:
        #[height(z), dim(y), width(x)]
        _x = x + direction[0]
        _y = y + direction[1]
        _z = z + direction[2]
        if (0<=_x<WIDTH) and (0<=_y<DIM) and (0<=_z<HEIGHT):
            if GRAPH[_z][_y][_x]==0:
                GRAPH[_z][_y][_x] = GRAPH[z][y][x] + 1
                cnt += 1
                edges.append([_x, _y, _z, RS+1])
if cnt == tomatos:
    print(RS)
else:
    print(-1)


