'''
https://www.acmicpc.net/problem/9370
후보지까지 거리가 같은 경로가 존재 할 때,
반드시 지나야하는 교차로를 지나는 경로가 무엇인지 체크!!
'''

import heapq
cases = int(input())

def bfs(start, cnt, must_pass):
    rs = [float('inf')] * (cnt+1)
    paths = [[] for _ in range(cnt+1)]
    queue = []
    heapq.heappush(queue, [0, start])
    paths[start].append(start)
    rs[start] = 0
    while queue:
        cur_dist, cur_v = heapq.heappop(queue)
        for next_v, dist in edges[cur_v]:
            new_dist = cur_dist + dist
            if new_dist < rs[next_v]:
                rs[next_v] = new_dist
                heapq.heappush(queue, [new_dist, next_v])
                paths[next_v] = paths[cur_v] + [next_v]
            elif new_dist == rs[next_v]:
                if (must_pass[0] in paths[next_v]) and (must_pass[1] in paths[next_v]):
                    pass
                else:
                    paths[next_v] = paths[cur_v] + [next_v]
                heapq.heappush(queue, [new_dist, next_v])

    return paths

for _ in range(cases):
    n, m, t = map(int, input().split()) # crossing, roads, candidates
    s, g, h = map(int, input().split()) # start, roads1, roads2

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, dist = map(int, input().split())
        edges[a].append([b, dist])
        edges[b].append([a, dist])

    candidates = []
    for _ in range(t):
        candidates.append(int(input()))

    paths = bfs(s, n, [g, h])
    rs = []
    for cand in candidates:
        if (g in paths[cand]) and (h in paths[cand]):
            rs.append(cand)
    rs.sort()
    print(' '.join([str(x) for x in rs]))
