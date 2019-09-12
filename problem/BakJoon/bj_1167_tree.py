def solution():
    def get_tree():
        n = int(input())
        v = [[] for i in range(n+1)]
        for k in range(n):
            p = [int(x) for x in input().split()[:-1]]
            for i in range(1, len(p), 2):
                if [p[i], p[i+1]] not in v[p[0]]:
                    v[p[0]].append([p[i], p[i+1]])
                if [p[0], p[i+1]] not in v[p[i]]:
                    v[p[i]].append([p[0], p[i+1]])
        return n, v

    def DFS(node, dist):
        global max_dist, max_node
        if visited[node]:
            return
        visited[node] = True
        if(max_dist < dist):
            max_dist = dist
            max_node = node
        for i in range(len(v[node])):
            DFS(v[node][i][0], dist+v[node][i][1])
        return

    n, v = get_tree()
    max_dist = 0
    max_node = 1
    visited = [False for _ in range(n+1)]
    DFS(max_node, max_dist)

    visited = [False for _ in range(n+1)]
    max_dist = 0
    DFS(max_node, max_dist)

    return max_dist


if __name__ == '__main__':
    print(solution())
