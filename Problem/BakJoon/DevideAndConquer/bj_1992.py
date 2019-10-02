'''
[devide and conquer]
https://www.acmicpc.net/problem/1992
'''
size = int(input())
arr = [[x for x in list(input())] for _ in range(size)]

rs = ''

def split_arr(arr):
    mid = len(arr)//2
    arr1 = [x[0:mid] for x in arr[0:mid]]
    arr2 = [x[mid:] for x in arr[0:mid]]
    arr3 = [x[0:mid] for x in arr[mid:]]
    arr4 = [x[mid:] for x in arr[mid:]]
    return arr1, arr2, arr3, arr4

def check_block(arr):
    tmp = arr[0][0]
    for r in arr:
        for c in r:
            if tmp != c:
                return False
    return True

def devide(arr):
    global rs
    if (len(arr) == 1) or check_block(arr):
        rs = rs + arr[0][0]
    else:
        arr1, arr2, arr3, arr4 = split_arr(arr)
        rs += '('
        devide(arr1)
        devide(arr2)
        devide(arr3)
        devide(arr4)
        rs += ')'
devide(arr)
print(rs)
