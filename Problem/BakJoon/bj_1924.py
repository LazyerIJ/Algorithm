inputMonth, inputDay = map(int, input().split())
mon_1 = [1,3,5,7,8,10,12]
mon_2 = [4,6,9,11]
mon_3 = [2]
mon_name = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sumDay = -1

for month in range(inputMonth):
    month += 1
    if month == inputMonth:
        sumDay += inputDay
        break
    else:
        if month in mon_1:
            sumDay += 31
        elif month in mon_2:
            sumDay += 30
        else:
            sumDay += 28
print(mon_name[sumDay%7],end='')



