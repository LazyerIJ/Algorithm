'''
https://www.acmicpc.net/problem/10830
- 행렬의 제곱
'''
#input
N, B = map(int, input().split(' '))
MAT = [[int(x) for x in input().split(' ')] for _ in range(N)]
#multiply matrix
def multiply_matrix(mat1, mat2):
    mat2 = list(zip(*mat2))
    rs = []
    for row in mat1:
        tmp = []
        for col in mat2:
            tmp.append(sum([a*b for a, b in zip(row, col)])%1000)
        rs.append(tmp)
    return rs
#basis matrix
rs = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    rs[i][i] = 1
#quare
tmp = MAT
while B>0:
    if B%2 == 1:
        rs = multiply_matrix(rs, tmp)
    B = B//2
    tmp = multiply_matrix(tmp, tmp)
#print
for r in rs:
    print(' '.join(list(map(str, r))))





