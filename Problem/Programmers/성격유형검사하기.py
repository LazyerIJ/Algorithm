# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def solution(survey, choices):
    answer = ''

    scores = {
            "RT": [0, 0],
            "CF": [0, 0],
            "JM": [0, 0],
            "AN": [0, 0]
            }
    for s, c in zip(survey, choices):
        target = scores.get(s)
        if target:
            if c < 4:
                target[0] += 4 - c
            else:
                target[1] += c - 4
        else:
            target = scores.get(s[::-1])
            if c < 4:
                target[1] += 4 - c
            else:
                target[0] += c - 4

    def get_target(key, value):
        if value[0] > value[1]:
            return key[0]
        elif value[1] > value[0]:
            return key[1]
        return sorted(key)[0]

    for target, score in scores.items():
        answer += get_target(target, score)
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

rs = solution(survey, choices)
print(rs)
