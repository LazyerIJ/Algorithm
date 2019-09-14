import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

road = '1'
block = '0'
graph = []

N, M = [int(x) for x in input().split(' ')]
for n in range(N):
    graph.append(list(input())[:-1])
dists = [[0]*M for _ in range(N)]

def get_edges(x, y, width=M, height=N,
              val=road, graph=graph):
    edges = []
    if (x < width-1) and (graph[y][x+1] == val):
        edges.append([x+1, y])
    if (x > 0) and (graph[y][x-1] == val):
        edges.append([x-1, y])
    if (y < height-1) and (graph[y+1][x] == val):
        edges.append([x, y+1])
    if (y > 0) and (graph[y-1][x] == val):
        edges.append([x, y-1])

    return edges

start_x, start_y = 0, 0
end_x, end_y = M-1, N-1

def bfs(start, graph, dists, end_x, end_y):
    queue = list()
    queue.append([start[0], start[1]])
    dists[start[1]][start[0]] = 0
    dist = 1
    while queue:
        dist += 1
        s = queue.pop(0)
        edges = get_edges(s[0], s[1])
        for edge in edges:
            if dists[edge[1]][edge[0]] == 0:
                queue.append([edge[0], edge[1]])
                dists[edge[1]][edge[0]] = dists[s[1]][s[0]] + 1

bfs([start_x, start_y], graph, dists, end_x, end_y)
print(dists[end_y][end_x] + 1)










