'''
MaxNonoverlappingSegments
https://app.codility.com/c/run/training7RQECR-B9E/
'''
def solution(A, B):
    if len(A)<=1:
        return len(A)
    rs = 1
    tail = B[0]
    for a, b in zip(A[1:], B[1:]):
        if a>tail:
            rs+=1
            tail = b
    return rs





    return rs

if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [1, 3, 7, 9, 9],
                     'B': [5, 6, 8, 9, 10]})
    rslist = []
    rslist.append([3])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

