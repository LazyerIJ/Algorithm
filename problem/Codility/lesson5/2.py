
def solution(S, P, Q):
    '''
    # score 62 / correcteness 100 / performance 0
    factors = {'A':1, 'C':2, 'G':3, 'T':4}
    rs = []
    myorder='ACGT'
    for (p, q) in zip(P, Q):
        rs.append(factors[sorted(S[p:q+1], key=myorder.index)[0]])
    return rs
    '''

    rs = []
    for (p, q) in zip(P, Q):
        if 'A' in S[p:q+1]:
            rs.append(1)
        elif 'C' in S[p:q+1]:
            rs.append(2)
        elif 'G' in S[p:q+1]:
            rs.append(3)
        else:
            rs.append(4)
    return rs


if __name__ == '__main__':
    import time

    testcase=[]
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]
    testcase.append([S, P, Q])

    for (S, P, Q) in testcase:
        START_TIME = time.time()
        print(solution(S, P, Q))
        print(time.time() - START_TIME)
