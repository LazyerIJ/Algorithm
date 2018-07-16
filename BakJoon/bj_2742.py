
count = int(input())
for step in range(count):
    print(count-step, end='')
    if step+1 < count:
        print()
