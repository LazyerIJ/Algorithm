def solution(N, A):
    '''
    #score 66 / correcteness 100 / performance 40
    rs = [0] * N
    for num in A:
        if num == N+1:
            max_num = max(rs)
            rs = [max_num] * N
        else:
            rs[num-1] += 1
    return rs
    '''

    '''
    #score 88 / correcteness 100 / performance 80
    rs = [0] * N
    cur_max=0
    for num in A:
        if num<=N:
            rs[num-1] += 1
            cur_max = cur_max if cur_max>rs[num-1] else rs[num-1]
        else:
            rs = [cur_max] * N
    return rs
    '''

    rs = [0] * N
    cur_max=0
    lowest = 0
    for num in A:
        if num<=N:
            rs[num-1] = rs[num-1] if rs[num-1]>lowest else lowest
            rs[num-1] += 1
            cur_max = cur_max if cur_max>rs[num-1] else rs[num-1]
        else:
            lowest = cur_max

    rs = [lowest if x<lowest else x for x in rs]
    return rs

if __name__ == '__main__':
    import numpy as np
    import time
    START_TIME = time.time()
    N = 100000
    A = np.random.randint(N, size=100001)
    rs = solution(N, A) # expected 6
    #print(rs)
    print(time.time() - START_TIME)

    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
