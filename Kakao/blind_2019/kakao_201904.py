def solution(food_times, k):
    from operator import itemgetter
    """solution

    :param food_times:
    :param k:
    """
    n_nums = len(food_times)
    food_dict = dict(zip(list(range(n_nums)), food_times))
    food_dict = sorted(food_dict.items(), key=itemgetter(1))
    total_time, idx = 0, -2
    for need_time in food_dict:
        total_time += need_time[1]
        if total_time > k:
            idx = need_time[0]
            break
    answer = idx+1
    return answer

if __name__ == '__main__':
    FOOD_TIMES = [3, 1, 2]
    k = 5
    print(solution(food_times=FOOD_TIMES, k=k))
