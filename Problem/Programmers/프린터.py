#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    priorities_indices = list(enumerate(priorities))
    priorities_max = sorted(priorities, reverse=True)
    cur_max = priorities_max.pop(0)
    cnt = 1
    while cnt < len(priorities):
        idx, priority = priorities_indices.pop(0)
        if priority >= cur_max:
            if idx == location:
                return cnt
            cnt += 1
            cur_max = priorities_max.pop(0)
        else:
            priorities_indices.append((idx, priority))
    return cnt


#print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
