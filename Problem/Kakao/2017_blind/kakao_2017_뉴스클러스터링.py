def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    def get_dict(str):
        str_dict = {}
        for idx in range(len(str)-1):
            key = str[idx:idx+2]
            count = str_dict.get(key, 0)
            str_dict[key] = count + 1
        return str_dict

    str1_dict = get_dict(str1)
    str2_dict = get_dict(str2)

    intersection_keys = str1_dict.keys() & str2_dict.keys()
    union_keys = str1_dict.keys() | str2_dict.keys()

    intersection_point = sum([min([str1_dict[x], str2_dict[x]]) for x
                             in intersection_keys if x.isalpha()])
    union_point = sum([max([str1_dict.get(x,0), str2_dict.get(x,0)]) for x
                             in union_keys if x.isalpha()])
    
    jacard = (intersection_point/union_point) if union_point!=0 else 1 

    return int(jacard*65536)


def solution2(str1, str2):
    import re
    import math
    str1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    str2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
                          

if __name__ == '__main__':
    str1 = 'FRANCE'
    str2 = 'french'
    rs = 16384
    print(rs, solution(str1, str2))

    str1 = 'handshake'
    str2 = 'shake hands'
    rs = 65536
    print(rs, solution(str1, str2))

    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    rs = 43690
    print(rs, solution(str1, str2))

    str1 = 'E=M*C^2'
    str2 = 'e=m*c^2'
    rs = 65536
    print(rs, solution(str1, str2))

