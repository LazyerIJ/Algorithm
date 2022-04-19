#https://programmers.co.kr/learn/courses/30/lessons/4274
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers_sorted = sorted(numbers, key=lambda x: (list(x)*3)[0:4], reverse=True)
    answer = "".join([str(x) for x in numbers_sorted])
    if int(answer) == 0:
        return "0"
    return answer

numbers = [6, 10, 2]
a1 = solution(numbers)
print(a1, "6210")
assert a1 == "6210"

numbers = [3, 30, 34, 5, 9]	
a2 = solution(numbers)
print(a2, "9534330")
assert a2 == "9534330"

print(solution([1000, 1, 10]), "101101000")
