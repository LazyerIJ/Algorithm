case = int(input())
result = ''
for step in range(case):
    re,num = input().split()
    for step2 in num:
        print(step2*int(re),end='')
    if step<case-1:
        print()
