def solution(s):
    rs = []

    def compress_n(s, n):
        #s를 n개 단위로 자름
        start = s[0:n]  #첫 n글자 확인
        rs = start # rs = 0
        idx = n #n부터 시작
        count = 1
        while n<len(s):
            cut = s[idx:idx+n]
            if start == cut:
                count += 1
                if idx+n>=len(s):
                    rs = rs + str(count)
                    break
            else:
                if count>1:
                    rs = rs + str(count) + cut
                else:
                    rs = rs + cut
                count = 1
            start = cut
            if idx+n>=len(s):
                break
            idx += n
        return len(rs)

    for n in range(1, len(s)+1):
        rs.append(compress_n(s, n))
    return min(rs)


if __name__ == '__main__':
    s = "aabbaccc"
    result = 7
    print(result, solution(s))

    s = "ababcdcdababcdcd"
    result = 9
    print(result, solution(s))

    s = "abcabcdede"
    result = 8
    print(result, solution(s))

    s = "abcabcabcabcdededededede"
    result = 14
    print(result, solution(s))

    s = "xababcdcdababcdcd"
    result = 17
    print(result, solution(s))
