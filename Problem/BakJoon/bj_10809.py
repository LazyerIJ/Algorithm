temp = input()
temp_list=[-1]*26
count=0
for step in temp:
    if temp_list[ord(step)-97]<0:
        temp_list[ord(step)-97]=count
    count+=1
result=''
for step in temp_list:
    result += str(step) + ' '
print(result[:-1],end='')
