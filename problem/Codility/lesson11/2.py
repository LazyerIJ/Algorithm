def solution(A):
    from math import sqrt
    A_max = max(A)
    A_len = len(A)
    #원소의 개수를 구한다.
    count = {}
    for element in A:
        count[element] = count.get(element, 0)+1
    #원소 별 약수를 구한다. 1은 모든 수의 공약수.
    divisors = {}
    for element in A:
        divisors[element] = [1]
    # 각 원소와 그 원소의 약수 최대값을 곱했을 때, max를 넘지 않게 하기 위해서
    # 최대값의 제곱근보다 작은 모든 약수를 구한다.
    for divisor in range(2, int(sqrt(A_max))+1):
        multiple = divisor
        while multiple <= A_max:
            #2~sqrt(A_max)의 수 중에서 divisors에 값이 존재할 때 만
            #and 이미 약수로 등록되있지 않을 때에만
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
    # 앞서 구한 약수에 대응되는 약수를 구한다.
    for element in divisors:
        temp = [element/div for div in divisors[element]]
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)
    result = []
    for element in A:
        result.append(A_len-sum([count.get(div, 0) for div in divisors[element]]))
    return result


if __name__ == '__main__':

    testcase = []
    testcase.append([1,2,3,4,5,6,7,8,9,10,20])
    rslist = []
    rslist.append([1,2,3,1,2,2,3,1,2,3])

    for case, rs in zip(testcase, rslist):
        myrs = solution(case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))
