#coding:utf-8

class Node(object):
    def __init__(self, item):
	self.elem = item
	self.next = None

class Tree(object):
    def __init__(self, node=None):
	self.root = node
	self.lchild = None
	self.rchild = None


	
