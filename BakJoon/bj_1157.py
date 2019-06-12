words = input().upper()
count_list = [0] * 26
for word in words:
    count_list[ord(word)-65] = count_list[ord(word)-65] + 1
max_count = max(count_list)
if count_list.count(max_count) == 1:
    print(chr(count_list.index(max_count) + 65))
else:
    print('?')


