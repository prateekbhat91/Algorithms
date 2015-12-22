"""
Binary Search Tree and its related functions

@author: Prateek Bhat
"""
"""Define a class to make objects for vertices"""

class node():

    def __init__ (self, id, parent = None):
        self.value = id
        self.parent = parent
        self.lchild = None
        self.rchild = None
        self.pos = None

"""Function to insert a new number in Binary tree"""
def insert(Rnode,num):
    if num > Rnode.value:
        if Rnode.rchild != None:
            insert(Rnode.rchild, num)
        else:
            child = node(num,Rnode)
            Rnode.rchild = child
    else:
        if Rnode.lchild != None:
            insert(Rnode.lchild,num)
        else:
            child = node(num, Rnode)
            Rnode.lchild = child

"""Print the Binary Tree in ascending order"""
def inordertreewalk(node):
    if node.lchild is not None:
        inordertreewalk(node.lchild)

    print node.value

    if node.rchild is not None:
        inordertreewalk(node.rchild)

"""Search for a particular node in Binary Tree"""
def search(rnode,num):

    if rnode.value == num:
            print "Number found"
            print "Number's parent = ",rnode.parent.value

    elif rnode.lchild != None or rnode.rchild != None:
            if rnode.value > num:
                search(rnode.lchild,num)
            else:
                search(rnode.rchild,num)

    else:
        print "Number not found in BST"


if __name__ == "__main__":
    rootnode = node(10)
    insert(rootnode,9)
    insert(rootnode,15)
    insert(rootnode,6)
    insert(rootnode,8)
    insert(rootnode,14)
    insert(rootnode,25)
    # inordertreewalk(rootnode)
    search(rootnode,25)