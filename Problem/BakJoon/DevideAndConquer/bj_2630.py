'''
https://www.acmicpc.net/problem/2630
'''
size = int(input())
num_white = num_blue = 0
arr = []

for i in range(size):
    arr.append([int(x) for x in list(input().split(' '))])

def check_block(arr):
    x = arr[0][0]
    for row in arr:
        for col in row:
            if x != col:
                return False
    return True

def split_arr(arr):
    new_size = len(arr)//2
    arr1 = [x[0:new_size] for x in arr[0:new_size]]
    arr2 = [x[0:new_size] for x in arr[new_size:]]
    arr3 = [x[new_size:] for x in arr[0:new_size]]
    arr4 = [x[new_size:] for x in arr[new_size:]]
    return arr1, arr2, arr3, arr4

def devide(arr):
    global num_blue, num_white
    if (len(arr) == 1) or check_block(arr):
        if arr[0][0] == 1 :
            num_blue += 1
        else:
            num_white += 1
    else:
        arr1, arr2, arr3, arr4 = split_arr(arr)
        devide(arr1)
        devide(arr2)
        devide(arr3)
        devide(arr4)

devide(arr)
print(num_white)
print(num_blue)


