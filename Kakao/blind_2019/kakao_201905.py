"""kakao_201905.py
길찾기
https://www.welcomekakao.com/learn/courses/30/lessons/42892?language=python3
"""
def solution(graph):

    if len(graph)==1:
        return [[1], [1]]

    #Node Class
    class Node:
        def __init__(self, data, val, left=None, right=None):
            self.left = left
            self.right = right
            self.data = data
            self.val = val

    def find_leaf(node, data):
        if data<node.data:
            if node.left:
                node = find_leaf(node.left, data)
            return node
        else:
            if node.right:
                node = find_leaf(node.right, data)
            return node
   
    #x좌표 입력 순서에 따른 데이터 값 = graph의 index 값
    graph_values = [i[0] for i in sorted(enumerate(graph),
                                         key=lambda x:x[1][1],
                                         reverse=True)]
    #입력해야 할 x 좌표 순서대로 정렬
    graph = graph.copy()
    graph = sorted(graph, key=lambda x: x[1], reverse=True)
    
    #x좌표와 데이터 값을 함께 저장
    head = Node(graph[0][0], graph_values[0] + 1)

    #길이가 1일 때

    #길이가 2 이상일 때
    for idx, data in enumerate(graph[1:]):
        data = data[0]
        node = find_leaf(head, data)
        if data<node.data:
            node.left = Node(data, graph_values[idx+1]+1)
        else:
            node.right = Node(data, graph_values[idx+1]+1)

    rs_in = []
    rs_post = []
    #전위순회
    def in_order_traversal(root):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                rs_in.append(root.val)
                _in_order_traversal(root.left)
                _in_order_traversal(root.right)
        _in_order_traversal(root)
    #후위순회
    def post_order_traversal(root):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                _in_order_traversal(root.right)
                rs_post.append(root.val)
        _in_order_traversal(root)

    
    in_order_traversal(head)
    post_order_traversal(head)
    return [rs_in, rs_post]


if __name__ == '__main__':
    NODE = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    RS = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    assert RS == solution(NODE)
