
class Stack(object):

    def __init__(self):
	self.item = []

    def push(self, elem):
	self.item.append(elem)
	return self.item

    def pop(self):
	self.item.pop()
	return self.item

    def peek(self):
	if self.is_empty():
	    print("This stack is empty")
        else:
	    return self.item[len(self.item)-1]

    def is_empty(self):
	return len(self.item) == 0

if __name__ == '__main__':
    stack = Stack()
    stack.is_empty()

    stack.push(100)
