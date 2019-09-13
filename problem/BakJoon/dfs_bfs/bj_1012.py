import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cases = int(input())

def get_edge(x, y, height, width):
    val = square[y][x]
    edges = []
    if (x-1 >= 0) and (square[y][x-1] == val):
        edges.append([x-1, y])
    if (y+1 < height) and (square[y+1][x] == val):
        edges.append([x, y+1])
    if (y-1 >= 0) and (square[y-1][x] == val):
        edges.append([x, y-1])
    if (x+1 < width) and (square[y][x+1] == val):
        edges.append([x+1, y])
    return edges

def find_start(visited):
    for y, vs in enumerate(visited):
        for x, v in enumerate(vs):
            if not v:
                return [x, y]
    return [-1, -1]

def dfs(x, y, N, M):
    if visited[y][x]:
        return
    visited[y][x] = True
    edges = get_edge(x, y, N, M)
    for edge in edges:
        dfs(edge[0], edge[1], N, M)

for case in range(cases):
    visited = []
    square = []
    rs = 0
    M, N, K = [int(x) for x in input().split(' ')]

    for n in range(N):
        square.append([0 for _ in range(M)])
        visited.append([False for _ in range(M)])
    for k in range(K):
        x, y = [int(x) for x in input().split(' ')]
        square[y][x] = 1

    while True:
        x, y = find_start(visited)
        if x == -1:
            break
        dfs(x, y, N, M)
        if square[y][x] > 0:
            rs += 1
    print(rs)




