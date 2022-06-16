#https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = list()
    calc_day = lambda x, y: round((100 - x) / y + 0.5, 0)
    left_day = calc_day(progresses[0], speeds[0])
    cnt = 1
    for progress, speed in zip(progresses[1:], speeds[1:]):
        days = calc_day(progress, speed) 
        if days > left_day:
            answer.append(cnt)
            left_day = days
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer

print(solution([93, 30, 55] , [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99] , [1, 1, 1, 1, 1, 1]))
print(solution([1, 10, 1, 1] , [90, 1, 1, 1]))


