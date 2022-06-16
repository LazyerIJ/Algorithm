#https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    for idx, citation in enumerate(sorted(citations, reverse=True)):
        if citation <= idx:
            return idx
    return len(citations)

print(solution([3,0,6,1,5]))
print(solution([1,1,1,1,1]))
