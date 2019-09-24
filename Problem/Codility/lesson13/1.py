def solution(A, B):
    max_L = max(A)
    rungs = [1] * (max_L+1)
    rs = []
    pos = {}
    for idx in range(2, max_L+1):
        rungs[idx] = rungs[idx-1] + rungs[idx-2]
    for a, b in zip(A, B):
        if not b in pos:
            pos[b] = (1<<b)-1
        rs.append(rungs[a]&pos[b])
    return rs



if __name__ == '__main__':

    testcase = []
    testcase.append({'A':[4, 4, 5, 5, 1], 'B':[3, 2, 4, 3, 1]})
    rslist = []
    rslist.append([1])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))

