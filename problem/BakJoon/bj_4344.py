input_num1 = int(input())
output=''
for step1 in range(input_num1):
    input_list = [int(x) for x in input().split()]
    numSum = sum(input_list[1:])
    numMean = numSum/input_list[0]
    count = sum([x>numMean for x in input_list[1:]])
    output += '%.3f'%(count/input_list[0]*100) + '%' + '\n'
print(output[:-1],end='')
