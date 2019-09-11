def solution(A):
    # Kadane Algorithm
    kadane_ending = [0] * len(A)
    kadane_starting = [0] * len(A)
    size = len(A)

    #save slice sum from head
    for num in range(1, len(A)):
        kadane_starting[num] = max(0, A[num]+kadane_starting[num-1])

        ###
        # >>kadane_starting[num] = max(A[num], A[num]+kadane_starting[num-1])
        # if max( 0 ->> A[num]) then slicesum should contains minus value
        # if minus value appear, we can move 'X' index
        # so that can make slicesum to zero which is bigger than minus
        ###

    #save slice sum from tail
    for num in range(len(A)-2, -1, -1):
        kadane_ending[num] = max(0, A[num]+kadane_ending[num+1])


    rs=0
    for num in range(1, size-1):
        rs = max(rs, kadane_starting[num-1]+kadane_ending[num+1])
        print(kadane_starting[num-1], kadane_ending[num+1])
    return rs
    

if __name__ == '__main__':
    testcase = []
    testcase.append([1,-2,2, -100,-200,10, 2])


    rslist = []
    rslist.append(17)

    for case, rs in zip(testcase, rslist):
        print(case)
        myrs = solution(case)
        print('mine: {}'.format(myrs))
        print('ans : {}'.format(rs))
        print('rs  : {}'.format(myrs==rs))
        print()
