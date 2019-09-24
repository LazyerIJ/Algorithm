count=int(input())
for step in range(count):
    none = ' '*(step)
    star = '*'*(count-step)
    print(none+star, end='')
    if step+1<count:
        print()
