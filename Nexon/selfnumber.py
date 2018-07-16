def is_selfnumber(n):
    for i in range(1,n):
        a = 0
        for j in str(i):
            a += int(j)
        a += i
        if a == n:
            return False
    return True
s = 0
for i in range(1,5000):
    if is_selfnumber(i):
        s += i
print(s)
