input_num1, input_num2 = map(int, input().split())
input_arr1 = input().split(' ')
result = ''
for step in range(input_num1):
    number = int(input_arr1[step])
    if number < input_num2:
        result += str(number) + ' '
print(result[:-1])
