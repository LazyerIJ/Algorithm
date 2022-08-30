# https://school.programmers.co.kr/learn/courses/30/lessons/118667


def solution(queue1, queue2):
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -1

    sum_a = sum(queue1)
    sum_b = sum(queue2)
    total = sum_a + sum_b

    if total %2 != 0:
        return answer

    for i in range(len(queue1) + len(queue2)):
        if sum_a == sum_b:
            return i
        if sum_a > sum_b:
            num = queue1.popleft()
            queue2.append(num)
            sum_a -= num
            sum_b += num
        elif sum_b > sum_a:
            num = queue2.popleft()
            queue1.append(num)
            sum_b -= num
            sum_a += num
    return answer


assert 2 == solution([3, 2, 7, 2], [4, 6, 5, 1] )
assert 7 == solution([1, 2, 1, 2], [1, 10, 1, 2])
assert -1 == solution([1, 1], [1, 5])

