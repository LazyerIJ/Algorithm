def solution(A):
    freq = 0
    leader = None
    tot_len = 0
    rs=0
    cnt=0

    if len(A)==1:
        return 0

    count = {}
    for idx, num in enumerate(A):
        if num in count.keys():
            count[num] += 1
            if count[num] > freq:
                freq = count[num]
                leader = num
        else:
            count[num] = 1
        tot_len += 1

    if freq*2<=tot_len:
        return 0

    size = len(A)
    for idx, num in enumerate(A):
        if num==leader:
            cnt+=1
        if cnt>((idx+1)/2) and (freq-cnt)>((size-idx-1)/2):
            rs+=1
    return rs






if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([4, 3, 4, 4, 4, 2])
    testcase.append([1, 4, 4, 4, 1, 4])

    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        #print(time.time() - START_TIME)
