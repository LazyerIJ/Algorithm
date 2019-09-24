'''
https://www.acmicpc.net/problem/2206
5 5
01000
00010
11110
11111
11110
'''
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
GRAPH = [[int(x) for x in input()[:-1]] for _ in range(N)]
DIRECTS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
VISITED = [[[0, 0] for _ in range(M)] for _ in range(N)]  # [chance / no cahce]

def bfs(cases):
    if not cases:
        return
    edges = []
    for x, y, chance in cases:
        for d_x, d_y in DIRECTS:
            _x = x + d_x
            _y = y + d_y
            if _x<0 or _x>=M or _y<0 or _y>=N:
                continue
            #벽인데 찬스가 있을 때
            if chance and GRAPH[_y][_x] == 1:
                if not VISITED[_y][_x][0]:
                    edges.append([_x, _y, 0])
                    #찬스를 쓴다
                    VISITED[_y][_x][0] += VISITED[y][x][1] + 1
            #길이 있을 때
            elif GRAPH[_y][_x] == 0:
                if not VISITED[_y][_x][chance]:
                    edges.append([_x, _y, chance])
                    VISITED[_y][_x][chance] += VISITED[y][x][chance] + 1
    bfs(edges)

VISITED[0][0] = [1, 1]
bfs([[0, 0, 1]])

rs = VISITED[-1][-1]
min_rs = min(rs)
if sum(rs)==0:
    print(-1)
else:
    if min_rs == 0:
        print(max(rs))
    else:
        print(min(rs))
