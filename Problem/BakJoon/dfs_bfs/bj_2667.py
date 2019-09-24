'''
https://www.acmicpc.net/problem/2667
'''
import sys
input = sys.stdin.readline

row = int(input())
square = []
visited = []
rs = weight = 0
rs_list = []

for r in range(row):
    square.append([int(x) for x in list(input()[:-1])])
    visited.append([False for _ in range(row)])

def get_edge(x, y, height=row, width=row):
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

def find_start():
    for y, vs in enumerate(visited):
        for x, v in enumerate(vs):
            if not v:
                return [x, y]
    return [-1, -1]

def dfs(x, y):
    global weight
    if visited[y][x]:
        return
    visited[y][x] = True
    weight += 1
    edges = get_edge(x, y)
    for edge in edges:
        dfs(edge[0], edge[1])

while True:
    x, y = find_start()
    if x==-1:
        break
    dfs(x, y)
    if square[y][x] > 0:
        rs += 1
        rs_list.append(weight)
    weight = 0
print(rs)
for rs in sorted(rs_list):
    print(rs)
