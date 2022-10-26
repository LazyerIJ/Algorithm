# https://school.programmers.co.kr/learn/courses/30/lessons/43105
summaries = [9999999999] * 500


def dp(summaries, layer):
    new_layer = list()
    for i, value in range(summaries):
        
        

def solution(triangle):
    summaries = list([0] * len(triangle))
    for i, t in enumerate(triangle):
        for j, l in enumerate(t):
            summaries[j] += l
        if i != 0:
            summaries[j] += t[-1]
        print(summaries)
    answer = min(summaries)
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

7
3 8
8 1 0
2 7 4 4
4 5 2 6 5