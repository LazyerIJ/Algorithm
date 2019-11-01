'''
https://www.acmicpc.net/problem/1676
10으로 나누려면.. 2*5 쌍이 나와야한다.
5가 나오기 전 반드시 짝수가 존재해서 2는 나온다.
그럼 5가 나오는 경우가 몇 번인지 보면 된다.
5의 제곱수에서 중복된 것을 함께 계산해주면 끝
'''
n = int(input())
flag = 5
rs = 0
while flag <= n:
    rs += n//flag
    flag = flag * 5
print(rs)
