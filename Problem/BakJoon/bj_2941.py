temp = input()
list1=['z','s','c']
list2=['n','l']
count = len(temp)
for step in range(len(temp)):
    if temp[step]=='=':
        if temp[step-1] in list1:
            count-=1
        else:
            count-=2
    elif temp[step]=='-':
        count-=1
    elif temp[step]=='j':
        if temp[step-1] in list2:
            count-=1
print(count, end='')
