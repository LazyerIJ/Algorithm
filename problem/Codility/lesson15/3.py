'''
https://app.codility.com/c/run/trainingQTHCNJ-QNZ/
'''
def solution(A):
    return len(set([abs(x) for x in A]))

if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [-5, -3, -1, 0, 3, 6]})
    rslist = []
    rslist.append([5])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

