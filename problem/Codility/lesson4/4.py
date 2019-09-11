def solution(A):
    '''
    # score 33 / correctness 20 / performance 50
    sorted_A = sorted(A)
    if sorted_A[-1]<=0:
        return 1
    for idx in range(1, len(A)):
        if sorted_A[idx]>0:
            if sorted_A[idx]-sorted_A[idx-1]>1:
                return sorted_A[idx-1]+1
    return sorted_A[-1]+1
    '''

    '''
    # score 55 / correctness 20 / performance 100
    sorted_A = sorted(A)
    if sorted_A[-1]<=0:
        return 1
    for idx in range(1, len(A)):
        if sorted_A[idx]>0 and sorted_A[idx-1]>0:
            if sorted_A[idx]-sorted_A[idx-1]>1:
                return sorted_A[idx-1]+1
    return sorted_A[-1]+1
    '''

    A = [x for x in A if x>0]
    if len(A)==0 or A[-1]<0:
        return 1
    def get_list(num):
        base = list(range(1, sorted_A[0]))
        base.append(num)
        return min(base)
    sorted_A = sorted(A)
    for idx, num in enumerate(sorted_A):
        if sorted_A[idx] - sorted_A[idx-1] > 1:
            return get_list(sorted_A[idx-1]+1)
    return get_list(sorted_A[-1]+1)


if __name__ == '__main__':
    import time
    START_TIME = time.time()
    print(solution([2])) # expected 6
    print(time.time() - START_TIME)
