n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

def gcd(a, b):
    if (a%b)==0:
        return b
    return gcd(b, a%b)

g = nums[1] - nums[0]
for i in range(2, n):
    g = gcd(g, nums[i]- nums[i-1])

rs = []
flag = 2
while True:
    if flag*flag > g:
        break
    if g%flag == 0:
        rs.append(flag)
        if flag != g//flag:
            rs.append(g//flag)
    flag += 1
rs.append(g)
rs.sort()

print(' '.join([str(x) for x in rs]))
