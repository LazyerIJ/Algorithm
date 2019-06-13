def solution(A):
    #rs = | head_sum - (sum_all - head_sum) |
    #rs = | sum_all - head_sum*2 |

    size = len(A)
    sum_all = sum(A)
    # head_sum_list
    sum_list = [A[0]]
    # rs_list
    rs_list = [abs(sum_all-((sum_list[0])*2))]
    for idx, val in enumerate(A[1:]):
        sum_list.append(sum_list[idx] + val)
        # sum_all - head_sum*2
        rs_list.append(abs(sum_all-((sum_list[idx]+val)*2)))
    return min(rs_list[:-1])


if __name__ == '__main__':
    print(solution([3,1,2,4,3]))
