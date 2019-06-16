def solution(A, B):
    # the elements of A are all distinct.
    # -> prevent A[N] == A[M]

    rs = [A.pop(0)]
    flag = [B.pop(0)]
    for a, b in zip(A, B):
        rs.append(a)
        flag.append(b)
        while True:
            if len(flag)<2:
                break
            pop_rs = rs.pop()
            pop_flag = flag.pop()
            if pop_flag<flag[-1]:  # 1: down 0: up
                if pop_rs>rs[-1]:
                    flag[-1] = pop_flag
                    rs[-1] = pop_rs
            else:
                rs.append(pop_rs)
                flag.append(pop_flag)
                break
    return len(rs)


if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([[4,5], [1,0]])

    for (A, B) in testcase:
        START_TIME = time.time()
        print(solution(A, B))
        #print(time.time() - START_TIME)
