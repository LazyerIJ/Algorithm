'''
https://www.acmicpc.net/problem/9375
쉽게 생각하자.
종류 1개 -> 아무것도 안고를 때 + 종류의 수 -> n+1

(n+1) * 종류의 수 - 하나도 고르지 않았을 때
'''
case = int(input())
for i in range(case):
    n = int(input())
    type_dict = {}
    for _ in range(n):
        name = input().split()[-1]
        num = type_dict.get(name, 1)
        type_dict[name] = num + 1
    arr = list(type_dict.values())
    rs = 1
    for i in arr:
        rs *= i
    print(rs-1)


