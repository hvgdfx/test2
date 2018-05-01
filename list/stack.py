
class Stack(object):

    def __init__(self):
	self.__item = []

    def push(self, elem):
	self.__item.append(elem)

    def pop(self):
	return self.__item.pop()

    def peek(self):
	if self.__item:
            return self.__item[-1]
	else:
	    return None
		
    def is_empty(self):
	return len(self.__item) == 0

    def size(self):
	return len(self.__item)


if __name__ == '__main__':
    stack = Stack()
    stack.is_empty()

    stack.push(100)




