input_num1 = int(input())
new_num = input_num1
count=0
while True:
    count+=1
    s1 = new_num//10
    s2 = new_num%10
    hop = (s1+s2) % 10
    new_num= s2*10 + hop
    if new_num == input_num1:
        break
print(count,end='')


