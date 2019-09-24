count = int(input())
for step in range(9):
    print('{0} * {1} = {2}'.format(count,(step+1),count*(step+1)), end='')
    if step+1 < 9:
        print()
