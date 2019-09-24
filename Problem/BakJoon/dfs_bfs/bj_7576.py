'''
https://www.acmicpc.net/problem/7576
뭔데 자꾸 시간초과...
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
RS = 0
WIDTH, HEIGHT = [int(x) for x in input().split(' ')]
VISITED = [[False]*WIDTH for _ in range(HEIGHT)]
GRAPH = []
tomatos = 0

for h in range(HEIGHT):
    tmp = [int(x) for x in input().split(' ')]
    GRAPH.append(tmp)
    tomatos += tmp.count(0)

def chk_start(val=1):
    return [[idx2,idx1]
            for idx1, y in enumerate(GRAPH)
            for idx2, x in enumerate(y)
            if GRAPH[idx1][idx2] == 1]

edges = chk_start()
cnt = 0
while True:
    tmp = []
    for edge in edges:
        for direction in directions:
            _x = edge[0] + direction[0]
            _y = edge[1] + direction[1]
            if (0<=_x<WIDTH) and (0<=_y<HEIGHT):
                if (GRAPH[_y][_x] == 0) and not VISITED[_y][_x]:
                    VISITED[_y][_x] = True
                    GRAPH[_y][_x] = 1
                    cnt += 1
                    tmp.append([_x, _y])
    edges = tmp
    if not edges:
        break
    RS += 1

if cnt == tomatos:
    print(RS)
else:
    print(-1)
