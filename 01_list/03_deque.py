
class Deque(object):

    def __init__(self):
	self.__item = []

    def add_front(self, elem):
        self.__item.insert(0, elem)

    def add_rear(self, elem):
	self.__item.append(elem)

    def pop_front(self):
	self.__item.pop(0)

    def pop_rear(self):
        self.__item.pop()

    def is_empty(self):
	return self.__item == []

    def size(self):
	return len(self.__item)

if __name__ == '__main__':
    queue = Deque()
    print(queue.is_empty())
    print(queue.size())

    queue.add_front(100)
    print(queue.is_empty())
    print(queue.size())
