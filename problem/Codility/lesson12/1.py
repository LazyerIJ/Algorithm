def solution(N, M):
    #Uclidien Algorithm
    #10, 4의 최대공약수는 2이다.
    #2의 배수 인덱스의 모든 초콜렛을 먹을 수 있다.
    def greatestCommonDivisor(n, m):
        if n%m==0:
            return m
        else:
            return greatestCommonDivisor(m, n%m)
    gcd = greatestCommonDivisor(N, M)
    if gcd==1:
        return N
    else:
        return int(N/gcd)

if __name__ == '__main__':

    testcase = []
    testcase.append({'N':10, 'M':4})
    rslist = []
    rslist.append([6])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))
