input_num1 = int(input())
input_str = input().split()
numSum=0
numMax=0
for step in range(input_num1):
    numSum += int(input_str[step])
    if int(input_str[step])>numMax:
        numMax=int(input_str[step])
print("%0.2f"%(numSum/input_num1 * 100/numMax))

