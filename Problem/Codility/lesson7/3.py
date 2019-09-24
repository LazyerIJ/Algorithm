def solution(S):
    rs = []
    for sym in S:
        if sym == '(':
            rs.append(1)
        else:
            if len(rs)==0:
                return 0
            rs.pop()
    return 1 if len(rs)==0 else 0


if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append("(()(())())")
    testcase.append("())")

    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        #print(time.time() - START_TIME)
