def solution(H):
    '''
    rs = [H.pop(0)]
    count = 1
    for wall in H:
        if wall==rs[-1]:
            continue
        elif wall>rs[-1]:
            rs.append(wall)
            count+=1
        elif wall<rs[-1]:
            idx=-2
            rs.append(wall)
            while idx>= ((-1 * len(rs))):
                if wall < rs[idx]:
                    idx -= 1
                    continue
                elif wall==rs[idx]:
                    break
                else:
                    count+=1
                    break
            if idx < -1*len(rs):
                count+=1
    return count
    '''
    block_cnt = 0

    stack = []

    for height in H:
        # remove all blocks that are bigger than my height
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()

        if len(stack) != 0 and stack[-1] == height:
            # we already paid for this size
            pass
        else:
            # new block is required, push it's size to the stack
            block_cnt += 1
            stack.append(height)

    return block_cnt



if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append([3,5,3,5,3,1])
    testcase.append([8,8,5,7,9,8,7,4,8])

    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        #print(time.time() - START_TIME)
