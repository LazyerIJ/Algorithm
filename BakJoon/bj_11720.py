length=int(input())
num=input()
numSum=0
for step in range(length):
    numSum+=int(num[step])
print(numSum,end='')
