'''
CountDistinctSlices
https://app.codility.com/c/run/trainingF96Y7V-YBA/
'''
def solution(M, A):
    rs = 0
    start = 0
    lastidx = [-1] * (max(A)+1)
    for idx, num in enumerate(A):
        idx+=1
        start = max(start, lastidx[num])
        lastidx[num] = idx
        rs += idx - start
    return min(rs, 1000000000)

if __name__ == '__main__':

    testcase = []
    testcase.append({'M': 6, 'A': [1,2,3,4,5,3,1,2,3,4,5]})
    testcase.append({'M': 10, 'A': [1,2,3,2,3]})
    testcase.append({'M': 10, 'A': [1,2,3,4,4,3]})
    rslist = []
    rslist.append([39])
    rslist.append([10])
    rslist.append([13])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

