import sys
sys.setrecursionlimit(10**7)

size = int(input())
rs = [0, 0, 0]
papers = [[int(x) for x in input().split(' ')] for _ in range(size)]


def check_same(arr):
    val = arr[0][0]
    for row in arr:
        for col in row:
            if val != col:
                return False, None
    return True, val


def count_paper(papers):
    if len(papers) == 1:
        rs[papers[0][0]] += 1
    else:
        flag, val = check_same(papers)
        if flag:
            rs[val] += 1
        else:
            width = len(papers)//3
            for i in [0, width, width*2]:
                for j in [0, width, width*2]:
                    count_paper([row[j:j+width] for row in papers[i:i+width]])

count_paper(papers)
print(rs[-1], rs[0], rs[1])
