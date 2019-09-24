def solution(K, M, A):
    #K 블록으로 나누고
    #A의 최대값은 M보다 크지 않으며
    #A의 K블록의각 합들 중 최대가 최소가되도록 한다
    #내가 못 푼 문제!!!!!

    def blockSizeIsValid(A, max_block_cnt, max_block_size):
        block_sum = 0
        block_cnt = 0
        for element in A:
            if block_sum + element > max_block_size:
                block_sum = element
                block_cnt += 1
            else:
                block_sum += element
            if block_cnt >= max_block_cnt:
                return False
        return True

    def binarySearch(A, max_block_cnt, M):
        lower_bound = max(A)
        upper_bound = sum(A)
        if max_block_cnt == 1:      return upper_bound
        if max_block_cnt >= len(A): return lower_bound
        while lower_bound <= upper_bound:
            candidate_mid = (lower_bound + upper_bound) // 2
            if blockSizeIsValid(A, max_block_cnt, candidate_mid):
                upper_bound = candidate_mid - 1
            else:
                lower_bound = candidate_mid + 1
        return lower_bound

    return binarySearch(A,K,M)




if __name__ == '__main__':

    testcase = []
    testcase.append({'K':3, 'M':5, 'A':[2, 1, 5, 1, 2, 2, 2]})
    rslist = []
    rslist.append([1])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))

