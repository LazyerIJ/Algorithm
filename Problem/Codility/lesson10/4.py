'''
https://app.codility.com/c/run/trainingWRN7CQ-SZA/
'''
def solution(A):
    '''
    # peak 중 최대 flag개수를 찾는다.
    # flag간의 거리는 flag개수보다 같거나 커야한다
    '''
    peaks = []

    for idx, num in enumerate(A[1:-1]):
        if A[idx] < A[idx+1] > A[idx+2]:
            peaks.append(idx)

    if len(peaks)<=2:
        return len(peaks)
    
    for num in range(len(peaks), 0, -1):
        #ex) flags num 10 ( == minisit dist 10) -> minimum range = 10*9
        if (peaks[-1]-peaks[0])//(num-1) < num:
            continue
        cur_peak = peaks[0]
        flags = 1
        for peak in peaks[1:]:
            if peak - cur_peak >= num:
                flags += 1
                cur_peak = peak
        if flags>=num:
            return num


if __name__ == '__main__':
    testcase = []
    testcase.append([1,5,3,4,3,4,1,2,3,4,6,2])
    testcase.append([1,2,1,2,1,2,1])
    rslist = []
    rslist.append(3)
    rslist.append(2)

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs))
        print('ans : {}'.format(rs))
        print()
