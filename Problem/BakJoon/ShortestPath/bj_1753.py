'''
https://www.acmicpc.net/problem/1753
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

heapq에 heappush를 할 때 (dist, v) 의 순서로 해야한다.
가까운 정점부터 순회하며 체크해야 하기 때문이다.
'''
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
edges = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    edges[u-1].append([v, w])

rs = ['INF' for _ in range(V)]
rs[start-1] = 0
queue = []
heapq.heappush(queue, [0, start])

while queue:
    dist, cur_v = heapq.heappop(queue)
    if (rs[cur_v-1] != 'INF') and (rs[cur_v-1]<dist):
        continue
    for next_v, weight  in edges[cur_v - 1]:
        r = dist + weight
        if (rs[next_v-1] == 'INF') or (r < rs[next_v - 1]):
            rs[next_v - 1] = r
            heapq.heappush(queue, [r, next_v])

for r in rs:
    print(r)
