'''
https://www.acmicpc.net/problem/2740
- 행렬 곱셈
'''
#input matrix
def input_matrix(size):
    arr = []
    for row in range(size):
        arr.append([int(x) for x in input().split(' ')])
    return arr

#rotate matrix B
def rotate_matrix(arr):
    return list(zip(*arr))

A_N, A_M = map(int, input().split(' '))
A = input_matrix(A_N)
B_N, B_M = map(int, input().split(' '))
B = rotate_matrix(input_matrix(B_N))
rs = []

for i, row in enumerate(A):
    #element wise multiply
    tmp = []
    for t in B:
        tmp.append(str(sum([a*b for a,b in zip(row,t)])))
    rs.append(' '.join(tmp))

for r in rs:
    print(r)
