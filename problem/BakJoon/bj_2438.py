count = int(input())
for step in range(count):
    print('*'*(step+1), end='')
    if step+1 < count:
        print()
