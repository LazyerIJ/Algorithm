import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

node_num, edge_num, start = [int(x) for x in input().split(' ')]

edges = [[] for _ in range(node_num + 1)]
for i in range(edge_num):
    a, b = [int(x) for x in input().split(' ')]
    edges[a].append(b)
    edges[b].append(a)

def dfs(node):
    if visited[node]:
        return
    print(node, end=' ')
    visited[node] = True
    s = sorted(edges[node])
    for to in s:
        dfs(to)

def bfs(graph, start):
    visit = list()
    queue = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            print(node, end= ' ')
            visit.append(node)
            queue.extend(sorted(graph[node]))

visited = [False for _ in range(node_num + 1)]
dfs(start)
print()
bfs(edges, start)



