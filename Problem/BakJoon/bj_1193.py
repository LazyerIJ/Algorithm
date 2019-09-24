num  = int(input())
summary  = 0
count = 0
while summary < num:
    count += 1
    summary += count
child = num-summary+count
parent = count+1-child
if count%2==1:
    temp=child
    child=parent
    parent=temp
print(str(child)+'/'+str(parent),end='')
