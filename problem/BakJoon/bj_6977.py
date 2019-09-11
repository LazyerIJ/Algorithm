sum_point = 0

for step in range(5):
    num = int(input())
    if num<40:
        num=40
    sum_point += num
print(int(sum_point/5), end='')
