#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for command in commands:
	sliced = sorted(array[command[0]-1:command[1]])
	answer.append(sliced[command[2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3]
        ]
answer = [5, 6, 3]

my_answer = solution(array, commands)
print(my_answer)
assert my_answer == answer
