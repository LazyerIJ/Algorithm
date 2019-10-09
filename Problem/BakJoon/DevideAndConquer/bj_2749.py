n = int(input())
basis = [[0, 1], [1, 1]]


def mul(mat1, mat2):
    mat = []
    mat2 = list(zip(*mat2))
    for m1 in mat1:
        tmp = []
        for m2 in mat2:
            val = sum([a*b for a, b in zip(m1, m2)]) % 1000000
            tmp.append(val)
        mat.append(tmp)
    return mat


def multiply(n):
    rs = [[0, 1], [1, 1]]
    flag = rs
    while n > 0:
        if n % 2 == 1:
            rs = mul(rs, flag)
        n = n // 2
        flag = mul(flag, flag)
    return rs


print(multiply(n-2)[-1][-1])

