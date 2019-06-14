def solution(A, B, K):
    return B//K - (A-1)//K


    return dist

if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([6, 11, 2]) # 3
    testcase.append([11, 345, 17]) # 20
    for (A, B, K) in testcase:
        START_TIME = time.time()
        print(solution(A, B, K))
        print(time.time() - START_TIME)
