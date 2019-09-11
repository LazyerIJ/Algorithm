def solution(key, lock):
    def rotate(key):
        return list(zip(*reversed(key)))
    
    def chk_key(my_key, lock):
        for step in range(4):
            my_key = rotate(my_key)
            cnt = 0
            for x in range(len(lock)):
                for y in range(len(lock)):
                    if my_key[x][y] != lock[x][y]:
                        cnt+=1
            if cnt==len(lock)*len(lock):
                return True
        return False

    w_key = len(key)
    w_lock = len(lock)

    #모든 경우의 수
    for x, x_idx in enumerate(range(0, w_lock-2+2*(w_key-1))):
        start_x = x_idx - w_key + 1#-2
        end_x = x_idx#0
        fill_head_x = max(0, start_x)
        fill_tail_x = w_key - end_x + 1

        for y, y_idx in enumerate(range(0, w_lock-2+2*(w_key-1))):
            start_y = y_idx - w_key + 1#-2
            end_y = y_idx#0
            fill_head_y = max(0, start_y)
            temp_key = list(reversed(key))[max(0,start_y):min(end_y+1, w_key)]
            fill_tail_y = w_lock - fill_head_y - len(temp_key)
            my_key = []
            for i in range(fill_head_y):
                my_key.append([0]*w_lock)
            for k in temp_key:
                t = []
                for i in range(fill_head_x):
                    t.append(0)
                t.extend(k[max([0, start_x]):min([end_x+1, w_key])])
                fill_tail_x = w_lock - len(t)
                for i in range(fill_tail_x):
                    t.append(0)
                my_key.append(t)
            for i in range(fill_tail_y):
                my_key.append([0]*w_lock)
            if chk_key(my_key, lock):
                return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(True, solution(key, lock))

key = [[0, 0, 0], [1, 0, 0],[ 1, 1,1]]	
lock = [[1, 1, 1,0], [1, 1, 0,1], [1, 0, 1,1],[0, 1, 1,1]]	
print(True, solution(key, lock))
