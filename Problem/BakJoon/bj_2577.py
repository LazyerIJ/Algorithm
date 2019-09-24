num1 = int(input())
num2 = int(input())
num3 = int(input())

multi = str(num1*num2*num3)
for step in range(9):
    print(multi.count(str(step)))
print(multi.count('9'),end='')
    

