import sys
input = sys.stdin.readline
meetings = []
num = int(input())
for _ in range(num):
    meetings.append([int(x) for x in input().split()])
meetings.sort(key=lambda x: [x[1], x[0]])
cnt = 0
end_time = 0
for meet in meetings:
    if meet[0]>=end_time:
        end_time = meet[1]
        cnt += 1
print(cnt)

