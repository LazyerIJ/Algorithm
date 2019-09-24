'''
https://programmers.co.kr/learn/courses/30/lessons/49993
'''
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        temp = []
        for i, s in enumerate(skill):
            if (s in st) and (len(temp) == i):
                    temp.append(st.index(s))
            else:
                break
        if temp and (temp == sorted(temp)):
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
rs = 2
print(rs, solution(skill, skill_trees))
