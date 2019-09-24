def solution(words):
    # timeout!!!!
    def count(str1, str2):
        num = 0
        step = min([len(str1), len(str2)])
        for idx in range(step):
            if str1[idx]!=str2[idx]:
                return idx
        return step

    words = sorted(words)
    rs = 1
    answer = 0
    for idx in range(1, len(words)):
        prev_len = len(words[idx-1])
        num = count(words[idx-1], words[idx])
        if num>=rs:
            rs = rs + num if rs+num<prev_len else prev_len 
        answer += rs
        rs = 1 + num
    return answer + 1 + num


def solution(words):
    ##?????
    def count(a, b):
        for i, char in enumerate(a):
            if len(b) == i or b[i] != char:
                return i+1
        else: return len(a)
    answer = 0
    words.append("")
    words.sort()
    for idx in range(1, len(words)):
        res = max(1, count(words[idx], words[idx-1]))
        if idx+1<len(words):
            res = max(res, count(words[idx], words[idx+1]))
        answer += res
    return answer


if __name__ == '__main__':
    words = ["go", "gone", "guild"]	
    result = 7
    print(result, solution(words))

    words = ["abc", "def", "ghi", "jklm"]	
    result = 4
    print(result, solution(words))

    words = ["word", "war", "warrior", "world"]	
    result = 15
    print(result, solution(words))

    words = ['agg', 'app', 'apple', 'azz']
    result = 11
    print(result, solution(words))
