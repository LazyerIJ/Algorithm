'''
https://app.codility.com/c/run/training5DPBD8-VYH/
CountTriangles
'''
def solution(A):
    A.sort()
    triangle_cnt = 0
    for x in range(0, len(A)-2):
        y = x + 1
        z = x + 2
        while (z < len(A)):
            if A[x] + A[y] > A[z]:
                triangle_cnt += z-y
                z += 1
            elif y < z - 1:
                    y += 1
            else:
                z += 1
                y += 1
    return triangle_cnt



if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [10, 2, 5, 1, 8, 12]})
    rslist = []
    rslist.append([4])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

