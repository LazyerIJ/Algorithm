numList=list(range(1,10000))
temp = list(range(1,10000))
for step1 in temp:
    number=str(step1)
    numlen=len(number)
    numSum=step1
    for step in range(numlen):
        numSum += int(number[step])
    if numSum in temp:
        try:
            numList.remove(numSum)
        except:
            pass

for step2 in numList[:-1]:
    print(step2)
print(numList[-1],end='')
