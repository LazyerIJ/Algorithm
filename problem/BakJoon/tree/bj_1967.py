import sys
sys.setrecursionlimit(10 ** 6)

num = int(sys.stdin.readline())
edges = [[] for _ in range(num+1)] # make node to index
max_weight = 0
max_node = 0

for i in range(num-1):
    node, dest, dist = [int(x) for x in sys.stdin.readline().split(' ')]
    edges[node].append([dest, dist])
    edges[dest].append([node, dist])

def dfs(node, dist):
    global max_weight, max_node
    if visited[node]:
        return
    visited[node] = True
    if max_weight < dist:
        max_weight = dist
        max_node = node
    for i in range(len(edges[node])):
        dfs(edges[node][i][0], edges[node][i][1] + dist)

visited = [False for _ in range(num+1)]
dfs(1, 0)
visited = [False for _ in range(num+1)]
dfs(max_node, 0)
print(max_weight)

#print(weight)







