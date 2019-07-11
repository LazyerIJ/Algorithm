def solution(N):
    rs = 0
    for i in range(1, N+1):
        div = N//i
        if div < i:
            break
        if N%i==0:
            if div==i:
                rs+=1
            else:
                rs+=2
    return rs 

if __name__ == '__main__':
    testcase = []
    testcase.append(24)
    testcase.append(1)
    testcase.append(25)
    testcase.append(169)
    rslist = []
    rslist.append(8)
    rslist.append(1)
    rslist.append(3)
    rslist.append(3)

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs), end='\t')
        print('rs  : {}'.format(myrs==rs))
