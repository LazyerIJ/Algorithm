def findPrime(num):
    
    for step in range(2,num):
        if num%step==0:
            return False
    
    return True

if __name__=='__main__':
    step = input()
    nums = input()
    nums = nums.split(' ')
    count_prime=0
    for num in nums:
        if int(num)==1:
            pass
        elif findPrime(int(num)):
            count_prime+=1
    print(count_prime)



