dim = int(input())
for step1 in range(dim):
    temp = input()
    point=0
    for step2 in temp.split('X'):
        for step3 in range(1,len(step2)+1):
            point += step3
    print(point,end='')
    if step1<dim-1:
        print()
    
