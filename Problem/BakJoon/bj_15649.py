'''
백트래킹
https://www.acmicpc.net/problem/15649
'''
N, M = map(int, input().split())
CHECK = [False] * (N+1)
ARR = [0] * M


def dfs(index, n, m):
    if index == m:
        for i in range(m):
            print(ARR[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if CHECK[i]:
            continue
        CHECK[i] = True
        ARR[index] = i
        dfs(index+1, n, m)
        CHECK[i] = False


dfs(0, N, M)
