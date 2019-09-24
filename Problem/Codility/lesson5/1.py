def solution(A):
    '''
    # score 20 / correcteness 40 / performance 0
    A.reverse()
    count = 0
    temp=0
    while True:
        try:
            idx = A.index(0)
            
            count = temp + len(A[:idx]) + count
            temp = len(A[:idx])
            A = A[idx+1:]
        except:
            return count
    return count
    '''
    try:
        A = A[A.index(0):]
    except:
        return 0
    i=0
    count=0
    count_sum=0
    for idx in range(0, len(A)):
        if A[idx]==1:
            count+=1*i
        else:
            i+=1
            count_sum += count
            if count_sum>1000000000:
                return -1
            count=0
    count_sum += count 
    if count_sum>1000000000:
        return -1
    return count_sum


        

if __name__ == '__main__':
    import time
    START_TIME = time.time()
    print(solution([0,1,0,1,1])) # expected 6
    print(time.time() - START_TIME)
