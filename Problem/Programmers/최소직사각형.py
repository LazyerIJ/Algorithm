# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(N):
    N_resized = list()
    for n in N:
        N_resized.append([max(n[0], n[1]), min(n[1], n[0])])
    return max([x[0] for x in N_resized]) * max([x[1] for x in N_resized])


arr = [[60, 50], [30, 70], [60, 30], [80, 40]]  
assert solution(arr) == 4000
arr = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]] 
assert solution(arr) == 120
arr = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] 
assert solution(arr) == 133
