# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    from itertools import permutations
    def flag(number):
        for i in range(2, number):
            if number%i == 0:
                return False
        return True
    arr = list()
    for i in range(1, len(numbers)+1):
        for number in permutations(numbers, i):
            num = int("".join(number))
            if num <= 1:
                continue
            if flag(num):
                arr.append(num)
    return len(set(arr))

assert solution("17") == 3
assert solution("011") == 2
