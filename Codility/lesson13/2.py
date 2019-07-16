def solution(A):

    def get_fib_seq_up_to_n(N):
        fib = [0] * (27)
        fib[1] = 1
        for i in range(2, 27):
            fib[i] = fib[i - 1] + fib[i - 2]
            if fib[i] > N:
                return fib[2:i]
    A.append(1)
    fib_set = get_fib_seq_up_to_n(len(A))
    reachable = [-1] * (len(A))
    #한 번에 갈수있는 곳 -> reachable 1
    for jump in fib_set:
        if A[jump-1] == 1:
            reachable[jump-1] = 1

    for idx in range(0, len(A)):
        if A[idx]==0 or reachable[idx]>0:
            continue
        temp_idx = -1
        temp_val = 123456789
        for jump in fib_set:
            if idx-jump < 0:
                break
            if 0<reachable[idx-jump]<temp_val:
                temp_val = reachable[idx-jump]
                temp_idx = idx-jump
        if temp_idx!=-1:
            reachable[idx]=temp_val+1
    return reachable[-1] 



if __name__ == '__main__':

    testcase = []
    testcase.append({'A':[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]}) # len 12
    testcase.append({'A':[0, 0, 0]}) # len 12
    rslist = []
    rslist.append([3])
    rslist.append([1])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))

