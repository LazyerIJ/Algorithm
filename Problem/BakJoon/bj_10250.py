cases = int(input())
for case in range(cases):
    H,W,N = map(int, input().split())
    N-=1
    floor = N%H+1
    roomNum = N//H+1
    if len(str(roomNum))==1:
        roomNum = '0' + str(roomNum)
    print(str(floor) + str(roomNum))

