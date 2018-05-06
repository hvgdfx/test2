
class Node(object):
    def __init__(self, item=None):
	self.elem = item
	self.prev = None
	self.next = None

class DoubleLinkList(object):

    def __init__(self, node=None):
	self.__head = node

    def is_empty(self):
	return self.__head is None

    def length(self):
	pass

    def travel(self):
	pass

    def add(self, item):
	pass

    def append(self, item):
	pass

    def insert(self, pos, item):
	pass

    def remove(self, item):
	pass



if __name__ == '__main__':

    node = Node(100)
    dll = DoubleLinkList(node)



