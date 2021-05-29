class Exceptions():
    pass


class TNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree to sort values as a tree,
    deviding values to less than on the left and greater than to the right
    containing methods like: 
        __int__(),
        __str__(),
        pre_order(),
        in_order(),
        post_order(),
    """

    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        """ Pre-order traversal of our tree root -> left -> right"""
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
        """ In-order traversal of our tree left -> root -> right"""

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
        """ Post-order traversal of our tree left -> right -> root """
        
        post_out = []
        def post(root):

            if root.left:
                post(root.left)

            if root.right:
                post(root.right)

            post_out.append(root.value)

        post(self.root)
        return post_out



if __name__ == "__main__":

    bt = BinaryTree(1)
    bt.root = TNode(5)
    bt.root.left = TNode(-4)
    bt.root.right = TNode(42)
    bt.root.left = TNode(4)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(-1)
    bt.root.right = TNode(14)
    bt.root.right.left = TNode(16)
    bt.root.right.right = TNode(20)
    print(bt.pre_order())
    print('\n\n************')
    print(bt.in_order())
    print('\n\n************')
    print(bt.post_order())


#################################################### K_ary treee node class...#######################################################
    
# # Think about
# class KNode:
#   def __init__(self, value=None):
#     self.value = value
#     self.children = []




################################################ a nother way to pre-order ##########################################################

#   def pre_order_iter(self):
#     stack = Stack()
#     stack.push(self.root)

#     while not stack.is_empty():
#       item = stack.pop()
#       print(item.value)

#       if item.right is not None:
#         stack.push(item.right)

#       if item.left is not None:
#         stack.push(item.left)
  
#   def bread_first(self):
#     # Use queque for FIFO
#     pass
