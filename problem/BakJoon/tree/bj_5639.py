'''
https://www.acmicpc.net/problem/5639
input에서 timeout 발생하는 듯 한..
'''
import sys
sys.setrecursionlimit(10 ** 6)

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        self._insert_data(self.root, data)

    def _insert_data(self, node, data):
        if data>node.data:
            if node.right:
                self._insert_data(node.right, data)
            else:
                node.right = Node(data)
        elif data<node.data:
            if node.left:
                self._insert_data(node.left, data)
            else:
                node.left = Node(data)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, root):
        if root == None:
            pass
        else:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.data)


bst = BinarySearchTree()
count = 0
while count <= 10000:
    try:
        key = int(sys.stdin.readline())
        if key < (10**6):
            bst.insert(key)
            count += 1
    except:
        break
bst.post_order()
