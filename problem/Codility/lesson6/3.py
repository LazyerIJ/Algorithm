def solution(A):
    A = sorted(A)
    for idx in range(0, len(A)-2):
        # A[idx], A[idx+1], A[idx+2] positive number check를 안했는데 통화
        if A[idx]+A[idx+1] > A[idx+2]:
            return 1
    return 0



if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([10, 2, 5, 1, 8, 20]) # 1, 2, 5, 8, 10, 20
    testcase.append([10, 50, 5, 1]) # 1, 5, 10, 50
    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        print(time.time() - START_TIME)
