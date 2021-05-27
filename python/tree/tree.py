from stacks_and_queues.stacks_and_queues import Stack, Queue


class TNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Search Tree to sort values as a tree,
    deviding values to less than on the left and greater than to the right
    containing methods like: 
    __int__(),
    __str__(),
    add(value),
    pre_order(),
    in_order(),
    post_order(),
    contains(value)
    """

    def __init__(self, root = None):
        self.root = root

    def __str__(self):
        pass

    def pre_order(self):
        """ Pre-order traversal of our tree """
        def pre(root):
            print(root.value)

            if root.left:
                pre(root.left)
            
            if root.right:
                pre(root.right)
                
        pre(self.root)

    def in_order(self):
        """ In-order traversal of our tree """
        def inorder(root):
            # print(root.value)

            if root:
                inorder(root.left)

                print(root.value)

                inorder(root.right)
  
        inorder(self.root)

    def post_order(self):
        """ Pre-order traversal of our tree """
        def post(root):
            if root:
                post(root.left)
        
                post(root.right)
        
                print(root.value),

        post(self.root)


class Binary_Search_Tree(BinaryTree):

    def add(self, root, value):
        if root is None:
            return TNode(value)
        else:
            if root.value == root:
                return root
            elif root.value < value:
                root.right = self.add(root.right, value)
            else:
                root.left = self.add(root.left, value)
        return root

    def contains(self, value): ## returns a boolean indicating whether or not the value is in the tree at least once 
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



if __name__ == "__main__":
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(4)
    node1.right.right = TNode(5)
    binary_tree = BinaryTree(node1)
    print ("\n\n\n\n\nPre-order traversal of binary tree is")
    binary_tree.pre_order()
    print ("\n\n\n\nInorder traversal of binary tree is")
    binary_tree.in_order()
    print ("\n\n\n\n\nPostorder traversal of binary tree is")
    binary_tree.post_order()
    
    # print ("\n\n\n\n\nPre-order traversal of binary tree is")
    print('\n\n\n\n\n\n')

    bst = Binary_Search_Tree(node1)
    bst.add(node1,1000)
    bst.add(node1,10000)
    bst.add(node1,-1)
    bst.add(node1, 56)
    bst.add(node1, 45)
    bst.add(node1, 6)
    bst.add(node1, 455)
    bst.add(node1, 78)
    bst.add(node1, 99)
    bst.add(node1, 21)
    bst.add(node1, 654)
    print(bst.contains(1000))
    print(bst.contains(-5))

    binary_tree.pre_order()

    
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