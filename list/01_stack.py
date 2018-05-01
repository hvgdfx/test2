
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
	return self.__item == []

    def size(self):
	return len(self.__item)


if __name__ == '__main__':
    stack = Stack()
    stack.is_empty()

    stack.push(100)
    stack.pop()

    print("success")

    print(stack.is_empty())
