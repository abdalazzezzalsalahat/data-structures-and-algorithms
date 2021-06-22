from .queue import Queue
class Exceptions():
    pass


class TNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    '''
    Binary Tree to sort values as a tree,
    deviding values to less than on the left and greater than to the right
    containing methods like: 
        __int__(),
        __str__(),
        pre_order(),
        in_order(),
        post_order(),
    '''

    def is_empty(self, root):
        if not root:
            return False


    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        ''' Pre-order traversal of our tree (root -> left -> right) '''
        pre_out = []
        def pre(root):
            pre_out.append(root.value)
            
            if root.left:
                pre(root.left)
            
            if root.right:
                pre(root.right)
                
        pre(self.root)

        return pre_out

    def in_order(self):
        ''' In-order traversal of our tree (left -> root -> right) '''

        in_out = []
        def walk(root):

            if root.left:
                walk(root.left)
            in_out.append(root.value)

            if root.right:
                walk(root.right)

        walk(self.root)
        return in_out

    def post_order(self):
        ''' Post-order traversal of our tree (left -> right -> root) '''
        
        post_out = []
        def post(root):

            if root.left:
                post(root.left)

            if root.right:
                post(root.right)

            post_out.append(root.value)

        post(self.root)
        return post_out

