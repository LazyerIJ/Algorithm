def solution(relation):
    """get cadidate keys in relation"""
    from itertools import combinations
    n_row = len(relation)
    n_col = len(relation[0])  #->runtime error 우려되는 부분

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final)
    for _, i in enumerate(range(len(final))):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)

if __name__ == '__main__':
    TEST_RELATION = [["100", "ryan", "music", "2"],
                     ["200", "apeach", "math", "1"],
                     ["300", "tube", "computer", "3"],
                     ["400", "con", "computer", "1"],
                     ["500", "ryan", "music", "3"],
                     ["600", "apeach", "music", "2"]]
    print(solution(TEST_RELATION))#2
