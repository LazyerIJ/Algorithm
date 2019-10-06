'''
https://www.acmicpc.net/problem/6549
- segment tree
- stack
'''
import sys
sys.setrecursionlimit(10**7)
def solution1():
    ##############timeout
    def get_max_area(start, end):
        if start >= end:
            return 0
        min_height = min(blocks[start:end])
        min_height_idx = blocks[start:end].index(min_height) + start
        area = min_height * (end-start)
        left_max = get_max_area(start, min_height_idx)
        right_max = get_max_area(min_height_idx+1, end)
        return max([area, left_max, right_max])
    while True:
        case = input()
        if case == '0':
            break
        blocks = [int(x) for x in case.split(' ')]
        size = blocks[0]
        blocks = blocks[1:]
        print(get_max_area(0, size))

def solution2():
    import math
    tree = None
    blocks = None
    def init(node, start, end):
        #Leaf node. Store Index.
        if start == end:
            tree[node] = start
        #Node not leaf
        else:
            #create child node
            init(node*2, start, (start+end)//2)
            init(node*2 + 1, (start+end)//2+1, end)
            #find child node (tree[node*2], tree[node*2]+1)
            #and select min value from blocks. store index (blocks[tree[...]])
            #store min value index (tree[node] = tree[node*2..])
            if blocks[tree[node*2]] <= blocks[tree[node*2+1]]:
                tree[node] = tree[node*2]
            else:
                tree[node] = tree[node*2 + 1]

    def query(node, start, end, i, j):
        '''query
        start~end 탐색 구간에서 i~j 탐색 범위가 존재하는지 확인.
        존재한다면 최소 값 반환.
        node: node
        start: 탐색 구간 왼쪽
        end: 탐색 구간 오른쪽
        i: 탐색 범위 왼쪽
        j: 탐색 범위 오른쪽
        '''
        #범위 확인
        if (i > end) or (j < start):
            return -1
        if (i <= start) and (j>=end):
            return tree[node]
        #트리의 왼쪽 가지 범위 체크
        m1 = query(2*node, start, (start+end)//2, i, j)
        #트리의 오른쪽 가지 범위 체크
        m2 = query(2*node+1, (start+end)//2+1, end, i, j)
        #구간이 오른쪽 가지에만 속하면
        if m1 == -1:
            return m2
        #구간이 왼쪽 가지에만 속하면
        elif m2 == -1:
            return m1
        #구간이 왼쪽과 오른쪽 가지를 일부 포함할 때 더 작은 값을 반환
        else:
            if blocks[m1] <= blocks[m2]:
                return m1
            else:
                return m2

    def largest(start, end):
        n = len(blocks)
        m = query(1, 0, len(blocks)-1, start, end)
        area = (end-start+1) * blocks[m]
        if start <= m-1:
            temp = largest(start, m-1)
            area = max(area, temp)
        if (m+1) <= end:
            temp = largest(m+1, end)
            area = max(area, temp)
        return area

    while True:
        case = input()
        if case == '0':
            break
        blocks = [int(x) for x in case.split(' ')]
        size = blocks[0]
        blocks = blocks[1:]
        tree_size = math.ceil(math.log2(size))
        tree = [0] * pow(2, tree_size+1)
        init(1, 0, size-1)
        print(largest(0, size-1))

solution2()

