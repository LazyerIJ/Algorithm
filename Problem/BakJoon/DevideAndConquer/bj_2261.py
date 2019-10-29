import math
def insort_left(a, x, lo=0, hi=None):
    key = x[1]
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][1] < key:
            lo = mid+1
        else: hi = mid
    a.insert(lo, x)

def bound(arr, key, thred):
    flag = None
    start = 0
    end = mid = len(arr)
    while (end-start) > 0:
        mid = (start+end)//2
        if thred=='lower':
            flag = arr[mid] < key
        elif thred == 'upper':
            flag = arr[mid] <= key
        if flag:
            start = mid+1
        else:
            end = mid
    return end

n = int(input())  # 2 <= num <= 100,000
points = []
start = 0
dist = lambda x, y: pow(y[1]-x[1], 2) + pow(y[0]-x[0], 2)

for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
points.sort()

rs = dist(points[0], points[1])
candidate = [points[0]]
insort_left(candidate, points[1])

for i in range(2, n):
    now = points[i]
    while start<i:
        cand = points[start]
        x = now[0] - cand[0]
        if x*x > rs:
            candidate.remove(cand)
            start += 1
        else:
            break
    d = int(math.sqrt(rs)) + 1
    lower_point = [-100000, now[1]-d]
    upper_point = [100000, now[1]+d]
    lower = bound(candidate, lower_point, thred='lower')
    upper = bound(candidate, upper_point, thred='upper')
    for i in range(lower, upper):
        d = dist(now, candidate[i])
        rs = d if d<rs else rs
    insort_left(candidate, now)

print(rs)






