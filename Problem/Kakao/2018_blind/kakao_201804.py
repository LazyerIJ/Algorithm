'''
https://www.welcomekakao.com/learn/courses/30/lessons/42891
reference : http://blog.naver.com/PostView.nhn?blogId=withham1&logNo=221365222338&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
'''
def solution(food_times, k):
    from operator import itemgetter

    #index를 추가하여 시간 순서대로 정렬해준다.
    #[[0, 시간], [1, 시간], [2, 시간], ... ]
    food_dict = dict(zip(list(range(len(food_times))), food_times))
    food_dict = sorted(food_dict.items(), key=itemgetter(1))
    size = len(food_dict)
    prev = 0

    '''
    k=14 / food_dict : [[2, 2], [4, 2], [0, 5], [3, 5], [1, 6]]
    1.소요시간이 2보다 큰 것은 5개 > 총 소요하는데 10 소요 > k(14)보다 작다
    2.k=14 >> k -= 10(2*5) >> k=4
    2.그 다음 값도 소요시간이 2이기 때문에 pass
    3.그 다음 값은 소요시간 > 소요시간 5지만 이전에 소요시간이 2인 것을 계산하였으므로 3으로 계산 > 소요시간 3 이상인 것 3개 > 총 소요에 9 필요 > k(4) 보다 크다.
    4.따라서 소요시간 5 이상인 것 중에 정답이 존재.
    5.소요시간 5 이상인 것에 대하여 %연산하여 index를 구한다.
    6.음식 번호 = index + 1
    7.return 음식 번호
    '''

    for idx, food in enumerate(food_dict):
        if prev!= None and prev==food[1]:
            continue
        k -= (food[1]-prev) * (size-idx)
        prev = food[1]
        if k < 0:
            food_dict = sorted(food_dict[idx:], key=itemgetter(0))
            return food_dict[k%len(food_dict)][0] + 1
    return -1


if __name__ == '__main__':
    FOOD_TIMES = [5,6,2,5,2]
    k = 14
    print(solution(food_times=FOOD_TIMES, k=k))
