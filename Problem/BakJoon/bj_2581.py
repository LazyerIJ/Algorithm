def findPrime(num):
    if num==1:
        return False
    for step in range(2,num):
        if num%step==0:
            return False
    return True

start = int(input())
end = int(input())

min_prime=None
sum_prime=0

for num in range(start, end+1):
    if findPrime(num):
        if min_prime==None:
            min_prime = num
        sum_prime += num

if min_prime:
    print(sum_prime)
    print(min_prime)
else:
    print(-1)
