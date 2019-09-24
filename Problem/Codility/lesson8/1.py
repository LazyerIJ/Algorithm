def solution(A):
    '''
    #score 66 correctness 100 performance 0
    if len(A)==0:
        return -1
    num = max(set(A), key=A.count)
    count = A.count(num)
    return A.index(num) if count/len(A)>0.5 else -1
    '''
    max_val = 0
    max_num = None
    max_idx = None
    tot_len = 0
    if len(A)==0:
        return -1
    elif len(A)==1:
        return 0

    count = {}
    for idx, num in enumerate(A):
        if num in count.keys():
            count[num] += 1
            if count[num] > max_val:
                max_val = count[num]
                max_num = num
                max_idx = idx
        else:
            count[num] = 1
        tot_len += 1
    if max_val*2>tot_len:
        return max_idx
    return -1




if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([3,4,3,2,3,-1,3,3])
    testcase.append([5])

    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        #print(time.time() - START_TIME)
