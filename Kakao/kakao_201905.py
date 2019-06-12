"""kakao_201905.py
https://www.welcomekakao.com/learn/courses/30/lessons/42892?language=python3
"""
def solution(nodeinfo):
    """solution

    :param nodeinfo:nodeinfo
    """
    def get_graph(node):
        node.sort(key=lambda x: x[1])
        return node

    def get_pre(node):
        return node

    def get_aft(node):
        return node

    graph = get_graph(nodeinfo)
    pre_search = get_pre(graph)
    aft_search = get_aft(graph)

    return [pre_search, aft_search]

if __name__ == '__main__':
    NODE = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    RS = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    assert RS == solution(NODE)
