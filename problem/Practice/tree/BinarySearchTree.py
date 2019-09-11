"""BinarySearchTree.py
BST : http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html
ORDER : http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-2.html
"""
class Node():
    """Node"""
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BInarySearchTree():
    """BInarySearchTree"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """insert

        :param data:data
        """
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        """find

        :param key:key
        """
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        if key < root.data:
            return self._find_value(root.left, key)
        return self._find_value(root.right, key)

    def delete(self, key):
        """delete

        :param key:key
        """
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False
        deleted = False
        if key == node.data:
            deleted = True
            #both left, right child
            if node.left and node.right:
                #the most deepest left node at right child node ->  root
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                #지우려고 하는 노드의 자식노드가 그 하위노드를 또 가지고 있을 때
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def pre_order_traversal(self):
        """DFT-pre_order_traversal
        node -> left child -> right child
        """
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    def in_order_traversal(self):
        """DFT-in_order_traversal
        left child -> node -> right child
        """
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def post_order_traversal(self):
        """DFT-post_order_traversal
        left child -> right child -> node
        """
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)

    def level_order_traversal(self):
        """BFT"""
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)


def run():
    """run"""
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    bst = BInarySearchTree()
    for val in array:
        bst.insert(val)
    print('[*]array >> {}'.format(array))
    print('[*]pre_order')
    bst.pre_order_traversal()
    print('[*]in_order')
    bst.in_order_traversal()
    print('[*]post_order')
    bst.post_order_traversal()
    print('[*]level_order')
    bst.level_order_traversal()

    print('[*]find 15>>{}'.format(bst.find(15)))
    print('[*]find 17>>{}'.format(bst.find(17)))
    print('[*]delete 55>>{}'.format(bst.delete(55)))
    print('[*]delete 14>>{}'.format(bst.delete(14)))
    print('[*]find 55>>{}'.format(bst.find(55)))
    print('[*]find 14>>{}'.format(bst.find(14)))


if __name__ == '__main__':
    run()
