def solution(N, stages):
    answer = []
    success, cur = [0] * N, [0] * N
    failed_dict = {}
    for stage in stages:
        if stage-1 != N:
            cur[stage-1] += 1
        else:
            stage = stage-1
        for idx in range(stage):
            success[idx] += 1
    for idx in range(N):
        if success[idx] == 0:
            failed_dict.update({idx:0})
        else:
            failed = cur[idx]/success[idx]
            failed_dict.update({idx:failed})
    answer = [x[0]+1 for x in sorted(failed_dict.items(), key=lambda x: x[1], reverse=True)]
    return answer
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(6, stages))
