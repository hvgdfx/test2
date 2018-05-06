#coding:utf-8

class Node(object):
    def __init__(self, item):
	self.elem = item
	self.next = None

class Tree(object):
    def __init__(self, node=None):
	self.tree = []
	self.lchild = None
	self.rchild = None

    def add(self, item):
	node = Node(item)
	if self.lchild == None:
	    

    def bread_order(self):
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


