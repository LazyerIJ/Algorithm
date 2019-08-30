'''
https://app.codility.com/c/run/trainingQRP9VG-XQA/
'''
def solution(A):
    marks = [A[0]]
    for square in A[1:]:
        marks.append(max(marks[-6:])+square)
    return marks[-1]

if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [1, -2, 0, 9, -1, -2]})
    rslist = []
    rslist.append([8])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

