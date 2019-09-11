num = input()
count=0
for step in num.lower():
    loc = ord(step)-97
    if loc <= 14:
        count += loc//3+2
    elif loc <= 18:
        count += 7
    elif loc <= 21:
        count += 8
    else:
        count += 9

print(count+len(num),end='')

