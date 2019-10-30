a, b = map(int, input().split())
u, v = max(a, b), min(a, b)
while u!=0:
    u, v = max(u, v), min(u, v)
    u = u-v
print(v)
print(a*b//v)

