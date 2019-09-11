def solution(A):
    # write your code in Python 3.6
    n_cols = len(A)
    n_rows = len(A[0])
    
    row_sum_dict = {}
    for row in A:
        key = sum(row)
        if key in row_sum_dict.keys():
            row_sum_dict[key] += 1
        else:
            row_sum_dict[key] = 1
    max_val = max(row_sum_dict, key=lambda k:row_sum_dict[k])
    flag = row_sum_dict[max_val]==1
    
    selected_row_sum_dict={}
    for i, row in enumerate(A):
        if sum(row)==max_val or flag:
            key = ''.join([str(x) for x in row])
            key_not = ''.join([str(int(not(x))) for x in row])
            if key in selected_row_sum_dict.keys():
                selected_row_sum_dict[key] += 1
            elif key_not in selected_row_sum_dict.keys():
                selected_row_sum_dict[key_not] += 1
            else:
                selected_row_sum_dict[key] = 1
    max_val = max(selected_row_sum_dict, key=lambda k:selected_row_sum_dict[k])
    return selected_row_sum_dict[max_val]



rs = solution([[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 1]])
print('result is : {}, answer is : {}'.format(rs, 2))
rs = solution(  [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
print('result is : {}, answer is : {}'.format(rs, 4))
