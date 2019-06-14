def solution(A):
    return len(set(A))


if __name__ == '__main__':
    import time
    testcase=[]
    testcase.append([1,1,2,2,3]) # 3
    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        print(time.time() - START_TIME)
