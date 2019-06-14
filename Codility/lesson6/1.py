def solution(A):
    # 가장 큰 수가 양수일 때, 무조건 포함되어야 한다
    # 최저값 2개, 최대값을 제외한 최대갑 2개의 크기 비교.
    # 가장 큰 수가 음수일 때는 절댓값이 최대한 작아야한다.
    A = sorted(A)
    return A[-1]*A[-2]*A[-3] if A[-1]<0 else A[-1] * max(A[0]*A[1], A[-2]*A[-3])


if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([-1, 1, 2, -2, 5, 6]) # 3
    testcase.append([-10, -7, -7, 2, 8, 10]) # 3
    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        print(time.time() - START_TIME)
