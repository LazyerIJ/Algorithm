from collections import Counter
from operator import itemgetter
import sys

input_list= []
input_len = int(sys.stdin.readline())

mysum=0

for step in range(input_len):
    t1 = int(sys.stdin.readline())
    input_list.append(t1)
    mysum+=t1

alist = sorted(input_list)
count = Counter(alist)
list_count = sorted(count.items(), key=itemgetter(1), reverse=True)
same_max=[]
max_value = max(count.values())
idx=0

try:
    while True:
        t1 = list_count[idx]
        if t1[1]==max_value:
            same_max.append(t1[0])
        else:
            break
        idx+=1
except:
    pass

same_max = sorted(same_max)
freq_value = same_max[bool(len(same_max)-1)]

result ='{0}\n{1}\n{2}\n{3}'.format(int(round(mysum/input_len,0)),alist[int(input_len/2)],freq_value,alist[input_len-1]-alist[0])

print(result)
