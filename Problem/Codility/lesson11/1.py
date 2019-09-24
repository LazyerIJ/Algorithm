def solution(N, P, Q):
    rs = []
    semiprimes = [0] * (N+1)
    flags = [0] * (N+1)
    for i in range(2, N+1):
        for j in range(i, int(N/i)+1):
            num1 = semiprimes[i]
            num2 = semiprimes[j]
            #multiply with primes
            if num1==0 and num2==0:
                semiprimes[i*j]+=1
            #else
            elif num1==0 or num2==0:
                semiprimes[i*j]+=2
    flags[0] = semiprimes[0]
    #particular summary
    for idx, semi in enumerate(semiprimes[1:]):
        if semi==1:
            flags[idx+1] = flags[idx] + 1
        else:
            flags[idx+1] = flags[idx]
    for p, q in zip(P, Q):
        rs.append(flags[q] - flags[p-1])
    return rs


if __name__ == '__main__':
    testcase = []
    testcase.append([26, [1, 4, 16], [26, 10, 20]])
    rslist = []
    rslist.append([10, 4, 0])

    for case, rs in zip(testcase, rslist):
        myrs = solution(case[0], case[1], case[2])
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))
