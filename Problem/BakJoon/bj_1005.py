"""bj_10005
https://www.acmicpc.net/problem/1005
"""
from sys import stdin
def get_max_route():
    """get_max_route

    :param graph:graph
    """
    #variables
    graphs = [[0, 0]]
    houses, conditions = map(int, stdin.readline().split(" "))
    times = [0] + list(map(int, stdin.readline().split(" ")))
    dp = times.copy()
    flag = 1
    #graph
    for _ in range(conditions):
        graphs.append(list(map(int, stdin.readline().split(" "))))
    graphs = sorted(graphs, key=lambda x: x[1])
    #target
    target = int(stdin.readline())
    for i in range(1, houses+1):
        condition_list = []
        while True:
            if flag < len(graphs) and graphs[flag][1] == i:
                condition_list.append(graphs[flag])
                flag = flag + 1
            else:
                break
        dp[i] = times[i] + max([dp[j[0]] for j in condition_list] + [0])
    return dp[target]

if __name__ == '__main__':
    test_case = int(stdin.readline())
    for case in range(test_case):
        print(get_max_route())

    
