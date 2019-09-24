def solution(A, B, C):
    '''
    정수 N개로 구성된 배열 A와 B가 있다.
    N개의 널판지를 의미한다.
    A[k]에서 시작해서 B[k]에서 끝난다.

    정수 M개로 구성된 배열 C가 있다.
    M개의 못을 의미한다.
    널판지의 C[k]에서 망치질을 할 수 있다.

    A[k]<=C[i]<=B[k] 이면 해당 널판지에 못질을 할 수 있다.
    모든 널판지에 못질이 될 수 있도록 하는 J번째 못 중에서
    최소값을 찾아라.
    '''

    rs = -1
    nailed = [False] * len(A)

    planks_size = max(B) - min(A) + 1
    flags = [False] * planks_size

    for idx, (a, b) in enumerate(zip(A, B)):



    for i, nail in enumerate(C):
        for idx, (a, b) in enumerate(zip(A, B)):
            if a<=nail<=b:
                nailed[idx]=True
                if sum(nailed)==len(A):
                    rs = i+1
                    return rs
    return rs




if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [1, 4, 5, 8], 'B':[4, 5, 9, 10],
                     'C':[4, 6, 7, 10, 2]})
    rslist = []
    rslist.append([1])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))

