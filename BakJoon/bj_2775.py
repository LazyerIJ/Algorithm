cases = int(input())

def summary(numList):
    summary=0
    total_list=[]
    for value in numList:
        summary += value
        total_list.append(summary) 
    return total_list

for case in range(cases):
    floor = int(input())
    rooom = int(input())
    total = 0
    if floor==0:
       total = rooom 
    else:
        num_total=list(range(1,rooom+1))
        for step1 in range(floor-1):
            num_total = summary(num_total) 
        total = sum(num_total)
    print(total)
