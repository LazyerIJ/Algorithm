'''
https://app.codility.com/c/run/training2TDWCV-7AP/
'''
def solution(A):
    from itertools import chain
    def getAbsDiff(t):
        return abs(t[0] + t[1])
    A.sort(key=abs)
    return getAbsDiff(min(chain(zip(A, A),zip(A,A[1:])),
                          key = getAbsDiff))

if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [1, 4, -3]})
    testcase.append({'A': [-8, 4, 5, -10, 3]})
    rslist = []
    rslist.append([1])
    rslist.append([3])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

