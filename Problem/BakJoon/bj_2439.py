import timeit
count = int(input())
start = timeit.default_timer()
for step in range(count):
    none = ' '*(count-step-1)
    star = '*'*(step+1)
    print(none+star,end='')
    if step+1 < count:
        print()
print(timeit.default_timer() - start)
