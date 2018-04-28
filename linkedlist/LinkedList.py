

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = next


'''

L = Node('a', Node('b', Node('c', Node('d'))))


'''

class SingleLinkedList(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
    def is_empty(self):
        pass
    def length(self):
        pass
    def travel(self):
        pass
    def add(self, pos, item):
        pass
    def append(self, item):
        pass
    def insert(self, pos, item):
        pass
    def remove(self, item):
        pass
    def search(self, item):
        pass
    



if __name__ == '__main__':
    print('success')