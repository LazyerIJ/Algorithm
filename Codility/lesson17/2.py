'''
MinAbsSum
https://app.codility.com/c/run/trainingUPJJNN-FUE/
'''
def solution(A):
    N = len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                    print('a', a, j, dp)
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
                    print('b', a, j, dp)
                else:
                    print('c', a, j, dp)

            print()
    print(dp)
    result = S
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            print('i: ', i)
            print('dp[i]: ', dp[i])
            print(S-2*i)
            result = min(result, S - 2 * i)
    return result

if __name__ == '__main__':

    testcase = []
    testcase.append({'A': [1, 1, 3]})
    rslist = []
    rslist.append([0])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))

