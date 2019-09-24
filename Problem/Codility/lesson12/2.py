def solution(A, B):
    #get greatest common divisors
    def gcd(x, y):
        if x%y == 0:
            return y;
        else:
            return gcd(y, x%y)

    #get smallest common divisors
    #ex(30, 10) -> 3(y:10, gcd:1) -> return 3 
    #ex(75, 15) -> 5(y:15, gcd:5) -> return 1
    def removeCommonPrimeDivisors(x, y):
        while x != 1:
            gcd_value = gcd(x, y)
            if gcd_value == 1:
                # x does not contain any more
                # common prime divisors
                break
            x /= gcd_value
        return x

    def hasSamePrimeDivisors(x, y):
        gcd_value = gcd(x, y)   # The gcd contains all
                                # the common prime divisors
        x = removeCommonPrimeDivisors(x, gcd_value)
        if x != 1:
            return False
        y = removeCommonPrimeDivisors(y, gcd_value)
        return y == 1

    count = 0
    for x,y in zip(A,B):
        if hasSamePrimeDivisors(x,y):
            count += 1
    return count


if __name__ == '__main__':

    testcase = []
    testcase.append({'A':[15, 10, 3], 'B':[75, 30, 5]})
    rslist = []
    rslist.append([1])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs))
