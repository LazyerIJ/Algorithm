def solution(A):

    if len(A)==1:
        return A[0]

    max_sum = A[0]
    cur_sum = A[0]

    for num in A[1:]:
        cur_sum += num #-1
        cur_sum = max(cur_sum, num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == '__main__':
    testcase = []
    testcase.append([-1, 1, 1])

    rslist = []
    rslist.append(5)

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs))
        print('ans : {}'.format(rs))
        print('rs  : {}'.format(myrs==rs))
        print()
