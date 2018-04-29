

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


'''

L = Node('a', Node('b', Node('c', Node('d'))))


'''

class SingleLinkedList(object):

    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, pos, item):
        cur = self.__head
        pass

    def append(self, item):
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)

    def insert(self, pos, item):
        pass
    def remove(self, item):
        pass
    def search(self, item):
        pass




if __name__ == '__main__':
    print('--------------------------')
    node = Node(100)
    singlelist = SingleLinkedList(node)
    singlelist.append(200)
    print('is empty: %s' %(singlelist.is_empty()))
    print('the length is %s' %(singlelist.length()))
    # singlelist.length()

    print('--travel begin--')
    print(singlelist.travel())
    print('--travel end----')
    print(node.next)

