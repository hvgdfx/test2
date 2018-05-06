#coding:utf-8

class Node(object):
    def __init__(self, item):
	self.elem = item
	self.next = None

class Tree(object):
    def __init__(self):
	self.tree = []
	self.lchild = None
	self.rchild = None

    def add(self, item):
	node = Node(item)
	if self.lchild == None:
	    self.lchild = node
	if self.rchild == None:
	    self.rchild = node	    	    
	


    def breath_order(self):
	pass

    def pre_order(self):
	pass

    def inorder(self):
	pass

    def post_order(self):
	pass	

if __name__ == '__main__':
    tree = Tree()
    print('build a tree')

    tree.add('a')




