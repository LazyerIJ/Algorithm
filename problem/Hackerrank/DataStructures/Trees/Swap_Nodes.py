#!/bin/python3

import os
import sys
#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    sys.setrecursionlimit(10**7)
    from collections import deque
    class node():
        def __init__(self, data, depth):
            self.data = data
            self.depth = depth
            self.left = None
            self.right = None
    def in_order(node, inorder=[]):
        if node.left and node.left.data != -1:
            in_order(node.left, inorder)
        inorder.append(node.data)
        if node.right and node.right.data != -1:
            in_order(node.right, inorder)

    root = node(1, 1)
    queue = deque()
    queue.append(root)
    
    #make tree
    while queue and indexes:
        tmp_node = queue.popleft()
        if tmp_node.data != -1:
            data = indexes.pop(0)
            tmp_node.left = node(data[0], tmp_node.depth + 1)
            tmp_node.right = node(data[1], tmp_node.depth + 1)
            if data[0] != -1:
                queue.append(tmp_node.left)
            if data[1] != -1:
                queue.append(tmp_node.right)


    #swap node
    rs = []
    for query in queries:
        inorder = []
        queue = deque()
        queue.append(root)
        while queue:
            tmp_node = queue.popleft()
            if tmp_node.depth % query == 0:
                tmp = tmp_node.left
                tmp_node.left = tmp_node.right
                tmp_node.right = tmp
            if tmp_node.left and tmp_node.left.data != -1:
                queue.append(tmp_node.left)
            if tmp_node.right and tmp_node.right.data != -1:
                queue.append(tmp_node.right)
        in_order(root, inorder)
        rs.append(inorder)
    print(rs)
    return rs



if __name__ == '__main__':
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

