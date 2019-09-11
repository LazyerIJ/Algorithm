def solution(A):
    '''
    #score 56 / correctness 100 / performance 12
    rs=0
    for idx1, num1 in enumerate(A[:-1]):
        count=0
        for idx2, num2 in enumerate(A[idx1+1:]):
            if idx2+idx1+1-num2<=idx1+num1:
                count+=1
        rs+=count
    return rs
    '''
    max_A = []
    min_A = []
    for idx, x in enumerate(A):
        max_A.append(idx+x)
        min_A.append(idx-x)

    # 원 왼쪽 최솟값
    min_A = sorted(min_A)
    # 원 오른쪽 최댓값
    max_A = sorted(max_A)

    rs=0
    min_idx=0
    count=len(A)

    for max_idx in range(0, count):
        while min_idx<count and max_A[max_idx]>=min_A[min_idx]:
            min_idx+=1
        rs += min_idx - max_idx - 1
        if rs > 10000000:
            return -1
    return rs


if __name__ == '__main__':
    import time
    testcase=[]
    testcase.append([1, 5, 2, 1, 4, 0]) # 3
    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        print(time.time() - START_TIME)
