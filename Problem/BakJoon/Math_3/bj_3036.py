n = int(input())
circles = list(map(int, input().split()))

def gcd(u, v):
    if u%v==0:
        return v
    return gcd(v, u%v)

base = circles[0]
for circle in circles[1:]:
    g = gcd(base, circle)
    print('{}/{}'.format(base//g, circle//g))
