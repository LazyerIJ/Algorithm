def solution(N):
    rs = 12345678910
    for i in range(1, N+1):
        div = N//i
        if div < i:
            break
        if N%i==0:
            rs = min(2*(div+i), rs)
    return rs 

if __name__ == '__main__':
    testcase = []
    testcase.append(30)
    rslist = []
    rslist.append(22)

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs), end='\t')
        print('rs  : {}'.format(myrs==rs))
