#coding:utf-8

class Node(object):
    def __init__(self, item):
	self.elem = item
	self.lchild = None
	self.rchild = None

class Tree(object):
    def __init__(self):
	self.root = None

    def add(self, item):
	node = Node(item)
	if self.root == None:
	    self.root = node
	    return 
	queue = [self.root]	
	while queue:
	    cur_node = queue.pop(0)
	    if cur_node.lchild is None:
                cur_node.lchild = node
          	return
	    else:
	        queue.append(cur_node.lchild)
            if cur_node.rchild is None:
	        cur_node.rchild = node
	        return
            else:
	        queue.append(cur_node.rchild)

    def breadth_order(self):
	queue = [self.root]

	if self.root is None:
	    return
	while queue:	
	    cur_node = queue.pop(0)
	    print(cur_node.elem),
	    if cur_node.lchild is not None:
	        queue.append(cur_node.lchild)
	    if cur_node.rchild is not None:
	        queue.append(cur_node.rchild)


    def pre_order(self, node):
	if node is None:
	    return
	print(node.elem),
	self.pre_order(node.lchild)
	self.pre_order(node.rchild)

    def in_order(self, node):
	if node is None:
	    return
	self.in_order(node.lchild)
	print(node.elem),
	self.in_order(node.rchild)

    def post_order(self, node):
	if node is None:
	    return
	self.post_order(node.lchild)
	self.post_order(node.rchild)
	print(node.elem),

if __name__ == '__main__':
    tree = Tree()
    print('build a tree')


    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)


    tree.breadth_order()
    print('\n')
    tree.pre_order(tree.root)
    print('\n')
    tree.in_order(tree.root)
    print('\n')
    tree.post_order(tree.root)





