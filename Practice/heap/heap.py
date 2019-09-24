import sys

class Heap:
    """Heap"""
    heap = []
    count = 0
    size = 0

    def __init__(self, size):
        """__init__

        :param size: heap size
        """
        self.heap = [-1 for i in range(0, size)]
        self.count = 0
        self.size = size

    def resizing(self):
        """resizing

        :param new: increasing size
        """
        for _ in range(self.size+1):
            self.heap.append(-1)
        self.size = self.size * 2  + 1

    def is_empty(self):
        """is_empty"""
        if not self.count:
            return True
        return False

    def is_full(self):
        """is_full"""
        if self.count is self.size:
            return True
        return False
    
    def insert_node(self, key):
        if self.is_full():
            self.resizing()

        if self.is_empty():
            self.heap[0] = key
            self.count += 1
        else:
            current_index = self.count
            # int(current_index/2): parent node index
            while (current_index/2 - 0.5) >= 0:
                # if key<parent node value -> break
                if key <= self.heap[int(current_index/2 - 0.5)]:
                    break
                # else parent node value -> child & current_index -> parent node
                self.heap[current_index] = self.heap[int(current_index/2 - 0.5)]
                current_index = int(current_index/2 - 0.5)
            self.heap[current_index] = key
            self.count += 1

    def delete_node(self):
        if self.is_empty():
            return 0

        # delete root and move last node to root
        delete_node = self.heap[0]
        tmp = self.heap[self.count-1]
        self.heap[0] = tmp
        self.heap[self.count-1] = -1
        self.count -= 1
        if self.is_empty():
            return delete_node

        current_node = 0
        child_node = current_node*2 + 1 # left child node
        #  if left child exist
        while child_node <= self.count:
            #  if right child exist
            if child_node + 1 <= self.count:
                # choose bigger one between left & right child
                if self.heap[child_node] <= self.heap[child_node + 1]:
                    child_node = child_node + 1
            if  tmp >= self.heap[child_node]:
                break
            self.heap[current_node] = self.heap[child_node]
            current_node = child_node
            child_node = 2 * child_node + 1
        self.heap[current_node] = tmp

        return delete_node

    def get_max(self):
        if self.count>0:
            return self.heap[0]
        else:
            return -1

    def get_min(self):
        if self.count>0:
            min_node = self.heap[self.size//2]
            for i in range(self.size//2+1, self.size):
                if self.heap[i] == -1:
                    continue
                min_node = min(min_node, self.heap[i])
            return min_node
        return -1

size = 10
heap = Heap(size)

print('[*]init heap: size={}'.format(size))
print()
for i in range(1, size+1):
    heap.insert_node(i)
    print('[*]insert: {}'.format(i))
    print('{}'.format(heap.heap))

print()

for i in range(int(size//4)):
    print('[*]delete: {}'.format(heap.delete_node()))
    print('{}'.format(heap.heap))
print()

print('[*]Heap.max>>\n{}'.format(heap.get_max()))
print('[*]Heap.min>>\n{}'.format(heap.get_min()))











