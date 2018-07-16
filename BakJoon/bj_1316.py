num = int(input())
count=0

for step in range(num):
    temp = input()
    chk = [True]*26
    chk[ord(temp[0])-97]=False

    for step1 in range(1,len(temp)):

        if chk[ord(temp[step1])-97] == False and temp[step1]!=temp[step1-1]:
            break

        chk[ord(temp[step1])-97] =False
        if step1 == len(temp)-1:
            count+=1

print(count,end='')

