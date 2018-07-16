input_num1 = int(input())
count=0
if input_num1<100:
    count = input_num1
else:
    count = 99
    for step1 in range(100,input_num1+1):
        subtract=int(str(step1)[0])-int(str(step1)[1])
        for step2 in range(1,len(str(step1))-1):
            temp=int(str(step1)[step2])-int(str(step1)[step2+1])
            print(step1,  ' ' , subtract , ' ' , temp)
            if subtract !=temp:
                break;
            count += 1
print(count,end='')




        
