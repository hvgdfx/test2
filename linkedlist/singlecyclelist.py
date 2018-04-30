#coding=utf-8

class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleList(object):
    def __init__(self, node = None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        if self.is_empty():
            return 0
        else:
            count = 1
            while cur.next == self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            #node.next = cur.next
            cur.next = node

    def insert(self, pos, item):
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() -1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count != pos:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if self.__head == cur:
                    #头结点
                    rear = self.__head
                    while rear != self.__head:
                        rear = rear.next
                    rear.next = cur.next
                    self.__head = cur.next
                else:
                    #中间结点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        #尾结点
        if cur.elem == item:
            pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False




if __name__ == '__main__':
    l1 = SingleCycleList()
    print(l1.is_empty())
    print(l1.length())

    l1.append(1)
    print(l1.is_empty())
    print(l1.length())

    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)

    l1.insert(-1, 9)
    l1.travel()
    l1.insert(3, 100)
    l1.travel()
    l1.insert(10,200)
    l1.travel()
    l1.remove(9)
    l1.travel()
    l1.remove(200)
    l1.travel()


