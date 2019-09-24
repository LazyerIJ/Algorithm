'''
https://www.acmicpc.net/problem/2263
'''
import sys
sys.setrecursionlimit(10 ** 6)

node_num = int(sys.stdin.readline())
in_order = [int(x) for x in sys.stdin.readline().split()]
post_order = [int(x) for x in sys.stdin.readline().split()]

position = [0] * (max(in_order)+1)
for idx, v in enumerate(in_order):
    position[v] = idx

def pre_order(in_start, in_end, post_start, post_end):

    if in_end < in_start or post_end < post_start:
        return
    root = post_order[post_end]
    print(root, end=' ')
    root_index = position[root]
    size = root_index - in_start

    pre_order(in_start, in_start + root_index-1,
              post_start, post_start + size - 1)

    pre_order(root_index+1, in_end,
              post_start + size, post_end-1)

pre_order(0, len(in_order)-1, 0, len(in_order)-1)
