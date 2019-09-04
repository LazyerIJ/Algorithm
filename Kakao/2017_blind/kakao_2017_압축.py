def solution(msg):
    answer = []
    dict_lzw = dict([[chr(i+65), i+1] for i in range(26)])
    idx = 0
    while idx<len(msg):
        flag = 1
        key = new_key = msg[idx]
        while (''.join(new_key) in dict_lzw):
            key = new_key
            new_key = msg[idx:idx+flag]
            flag += 1
            if idx==len(msg)-len(key):
                break
        answer.append(dict_lzw[''.join(key)])
        dict_lzw[''.join(new_key)] = len(dict_lzw)+1
        if idx==len(msg)-1:
            break
        idx += flag-2
    return answer


if __name__ == '__main__':
    msg = "KAKAO"
    answer = [11, 1, 27, 15]
    #print(answer, solution(msg))

    msg = "TOBEORNOTTOBEORTOBEORNOT"
    answer = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    print(answer, solution(msg))

    msg = "ABABABABABABABAB"
    answer = [1, 2, 27, 29, 28, 31, 30]
    print(answer, solution(msg))
