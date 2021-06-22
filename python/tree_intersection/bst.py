from .tree import *


class Binary_Search_Tree(Binary_Tree):
    """
    Binary Search Tree class to add new element to a binary tree, 
    and search for a spisific element in a binary tree.
    fnctions: 
        add(value),
        contains(value)
    """

    def add(self, value):
        """
        Add that accepts a value, and adds a new node with that value in the correct location
        in the binary search tree.
        """        
        if not self.root:
            self.root = TNode(value)
        else:
            def walk(roots):
                if value < roots.value:
                    if not roots.left:
                        roots.left = TNode(value)
                        return
                    else:
                        walk(roots.left)
                else:
                    if not roots.right:
                        roots.right = TNode(value)
                        return
                    else:
                        walk(roots.right)
            walk(self.root)

    def contains(self, value):
        ''' Return Boolean indicating existence (but not location) of value on tree '''
        if not self.root:
            return False
        current = self.root
        while True:
            if value == current.value:
                return True
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False

