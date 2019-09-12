node_size = int(input())

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None

def find_node(root, data):
    if root.data == data:
        return root
    if root.left:
        node = find_node(root.left, data)
        if node != None:
            return node
    if root.right:
        node = find_node(root.right, data)
        if node != None:
            return node
    
root = None
for num in range(node_size):
    data, left, right = input().split()
    node = Node(data)
    if root == None:
        root = node
    rs = find_node(root, data)
    if left != '.':
        rs.left = Node(left)
    if right != '.':
        rs.right = Node(right)

def _order_traversal(root, mode):
    if root is None:
        pass
    else:
        if mode=='pre':
            print(root.data, end='')
        _order_traversal(root.left, mode)
        if mode=='mid':
            print(root.data, end='')
        _order_traversal(root.right, mode)
        if mode=='post':
            print(root.data, end='')

_order_traversal(root, 'pre')
print()
_order_traversal(root, 'mid')
print()
_order_traversal(root, 'post')





