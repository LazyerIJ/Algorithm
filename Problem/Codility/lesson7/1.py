def solution(S):
    rs = []
    start_sym = ["(", "[", "{"]
    end_sym = [")", "]", "}"]
    for symbol in S:
        print(rs, symbol)
        if symbol in start_sym:
            rs.append(symbol)
        elif len(rs)!=0 and symbol == end_sym[start_sym.index(rs[-1])]:
            rs.pop()
        else:
            return 0
    return 1 if len(rs)==0 else 0




if __name__ == '__main__':
    import time

    testcase=[]
    testcase.append("][")
    testcase.append("[][")

    for A in testcase:
        START_TIME = time.time()
        print(solution(A))
        #print(time.time() - START_TIME)
