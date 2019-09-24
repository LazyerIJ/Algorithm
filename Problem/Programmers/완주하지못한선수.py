'''
https://www.welcomekakao.com/learn/courses/30/lessons/42576
'''
def solution(participant, completion):
    #remove, pop 등으로 하면 시간 초과
    participant.sort()
    completion.sort()
    for idx in range(0, len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
    return participant[-1]
