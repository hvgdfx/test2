
class Queue(object):

    def __init__(self):
	self.__item = []

    def enqueue(self, elem):
	self.__item.append(elem)

    def dequeue(self):
        self.__item.pop()

    def is_empty(self):
	return self.__item == []

    def size(self):
	return len(self.__item)

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    print(queue.size())

    queue.enqueue(100)
    print(queue.is_empty())
    print(queue.size())
