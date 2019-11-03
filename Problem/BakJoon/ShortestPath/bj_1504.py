'''
https://www.acmicpc.net/problem/1504
- 양방향 그래프 주의
- 이렇게 따로따로 모두 계산해도 됨..;;
- 경로를 체킹해야 하는 줄 알았는데..
'''
import sys
input = sys.stdin.readline
import heapq
N, E = map(int ,input().split())
edges = [[] for _ in range(N)]
for _ in range(E):
    v_from, v_to, dist = map(int, input().split())
    edges[v_from-1].append([v_to, dist])
    edges[v_to-1].append([v_from, dist])
paths = list(map(int, input().split()))

def bfs(start, end):
    rs = [float('inf') for _ in range(N)]
    rs[start-1] = 0

    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        cur_dist, cur_v = heapq.heappop(queue)
        for next_v, dist in edges[cur_v - 1]:
            new_dist = cur_dist + dist
            if new_dist < rs[next_v - 1]:
                rs[next_v - 1] = new_dist
                heapq.heappush(queue, [new_dist, next_v])
    return rs[end-1]

rs1 = bfs(1, paths[0]) + bfs(paths[0], paths[1]) + bfs(paths[1], N)
rs2 = bfs(1, paths[1]) + bfs(paths[1], paths[0]) + bfs(paths[0], N)
rs = min(rs1, rs2)
print(rs if rs != float('inf') else -1)




