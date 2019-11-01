'''
https://www.acmicpc.net/problem/2004
nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
'''

def devide_ten(num, key):
    flag = key
    rs = 0
    while flag <= num:
        rs += num//flag
        flag = flag * key
    return rs
N, M = map(int ,input().split())
key=5
rs_5 = devide_ten(N, key) - devide_ten(M, key) - devide_ten(N-M, key)
key=2
rs_2 = devide_ten(N, key) - devide_ten(M, key) - devide_ten(N-M, key)
print(min(rs_5, rs_2))


