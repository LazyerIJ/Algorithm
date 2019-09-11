import timeit
count = int(input())
start = timeit.default_timer()
for step in range(count):
    none= ' '*(step)
    star = '*'*(count-step)
    print(none+star,end='')
    if step+1 < count:
        print()
print(timeit.default_timer() - start)
