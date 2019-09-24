weight = int(input())
temp=True
num5 = weight//5
left5 = weight%5
while num5>=0:
    if left5%3 ==0:
        print(num5+left5//3,end='')
        temp=False
        break
    num5 -=1
    left5 += 5
if temp:
    print(-1,end='')




