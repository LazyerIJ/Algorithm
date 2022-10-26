# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    from itertools import cycle
    size = len(answers)
    user_1 = [1, 2, 3, 4, 5]
    user_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    user_1_answer = sum([x==y for x, y in zip(cycle(user_1), answers)])
    user_2_answer = sum([x==y for x, y in zip(cycle(user_2), answers)])
    user_3_answer = sum([x==y for x, y in zip(cycle(user_3), answers)])
    max_point = max(user_1_answer, user_2_answer, user_3_answer)
    if user_1_answer == max_point:
        answer.append(1)
    if user_2_answer == max_point:
        answer.append(2)
    if user_3_answer == max_point:
        answer.append(3)
    return answer


arr = [1, 2, 3, 4, 5]
assert solution(arr) == [1]
arr = [1, 3, 2, 4, 2]
assert solution(arr) == [1, 2, 3]
