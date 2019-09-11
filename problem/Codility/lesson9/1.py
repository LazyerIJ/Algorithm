def solution(A):
    if len(A)==0:
        return 0
    elif len(A)==1:
        return A[0]

    def dynamic_split(A, candidates):
        max_num = max(A)
        min_num = min(A)
        max_num_idx = A.index(max_num)
        min_num_idx = A.index(min_num)

        if max_num_idx<min_num_idx:
            A_split1 = A[:max_num_idx]
            A_split2 = A[max_num_idx+1:min_num_idx]
            A_split3 = A[min_num_idx:]
            if len(A_split1)>0:
                cand1 = max_num - min(A_split1)
                candidates.append(cand1)
            if len(A_split2)>0:
                cand2 = dynamic_split(A_split2, candidates)
                candidates.append(cand2)
            if len(A_split3)>0:
                cand3 = max(A_split3) - min_num
                candidates.append(cand3)
        else:
            candidates.append(max_num-min_num)
        return max(candidates)
    return dynamic_split(A, [])







if __name__ == '__main__':
    testcase = []
    testcase.append([23171, 21011, 21123, 21366, 21013, 21367])
    testcase.append([20, 30, 40, 100, 3, 25, 88, 1, 90, 10, 80])
    testcase.append([10, 1])

    rslist = []
    rslist.append(356)
    rslist.append(89)
    rslist.append(0)

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs), end='\t')
        print('rs  : {}'.format(myrs==rs))
