room = input()
lists = [0]*10
for step in room:
    if step =='6':
        step = '9'
    lists[int(step)]+=1
lists[9] = lists[9]//2+lists[9]%2
print(max(lists))

