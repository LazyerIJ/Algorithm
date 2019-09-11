input_str=input()
length=len(input_str)
for step in range(0,length//10):
    print(input_str[:10])
    input_str=input_str[10:]
print(input_str,end='')
