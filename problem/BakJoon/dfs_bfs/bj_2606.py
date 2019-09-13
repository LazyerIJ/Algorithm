import sys
input = sys.stdin.readline
num = int(input())
edge_num = int(input())

edges = [[] for _ in range(num+1)]
visited = [[] for _ in range(num+1)]

for _ in range(edge_num):
    a, b = [int(x) for x in input().split(' ')]
    edges[a].append(b)
    edges[b].append(a)

def bfs(graph, count=0, start=1):
    visited = list()
    queue = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            count += 1
    return count

print(bfs(edges) - 1)




