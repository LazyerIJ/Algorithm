def solution(X, A):

    '''
    # score: 50 / correctness: 100 / performance: 0
    flag = [False] * X
    for idx, num in enumerate(A):
        if num<=X:
            flag[num-1] = True
        if sum(flag) == X:
            return idx
    return -1
    '''

    # score: 100 / correctness: 100 / performance: 100
    flag = [False] * X
    count = 0
    for idx, num in enumerate(A):
        if num<=X:
            if not flag[num-1]:
                flag[num-1] = True
                count +=1
            if count==X:
                return idx
    return -1


if __name__ == '__main__':
    import time
    START_TIME = time.time()
    print(solution(10,[1,2,3,4,5,6,11,7,8,9,10])) # expected 6
    print(time.time() - START_TIME)
