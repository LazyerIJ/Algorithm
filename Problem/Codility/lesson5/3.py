def solution(A):
    '''
    # score 50 / correcteness 100 / performance 0
    sum_tota = []

    for idx_start in range(0, len(A)-1):
        sum_rows=[]
        for i, idx_end in enumerate(range(idx_start+1, len(A))):
            split = A[idx_start:idx_end+1]
            sum_rows.append(sum(split)/(i+2))
        sum_tota.append(min(sum_rows))
    return sum_tota.index(min(sum_tota))
    '''

    '''
    # score 60 / correcteness 100 / performance 20
    rs=-1
    minist = 123456789
    for i in range(0, len(A)-1):
        sum=A[i]
        min=123456789
        for idx, j in enumerate(range(1, len(A)-i)):
            sum += A[i+j]
            min = min if sum/(idx+2) > min else sum/(idx+2)
        if minist>min:
            rs = i
            minist=min
    return rs
    '''

    # 지금까지 모든 겨우의 수만 생각하려고 했던...
    # 최소 평균은 길이가 2 또는 3인 집합에 대해서만 고려하면 되는거였다..
    # 왜 몰랐을까..
    min_avg = 123456789
    rs = -1
    for idx in range(0, len(A)-2):
        avg_2 = (A[idx]+A[idx+1])/2
        avg_3 = (avg_2 * 2 + A[idx+2])/3
        avg = min(avg_2, avg_3)
        if avg<min_avg:
            rs = idx
            min_avg = avg
    if min_avg>((A[-1]+A[-2])/2):
        rs = len(A)-2
    return rs



if __name__ == '__main__':
    import time

    testcase=[]
    A = [4, 2, 2, 5, 1, 5, 8]
    testcase.append(A)
    print(A)
    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        print(time.time() - START_TIME)
