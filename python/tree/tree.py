from stacks_and_queues.stacks_and_queues import Queue

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

    ################## CC 16 Find Maximum Value ##################
    
    def find_maximum_value(self, node = None, result=[]):
        '''
        Find Maximum Value a function that returns the maximum value stored in a tree.
        '''        
        max_val = 0

        if not self.root:
            return max_val

        result = []
        result.append(self.root)

        while result:
            current_node = result.pop(0)

            if current_node.value > max_val:
                max_val = current_node.value

            if current_node.left:
                result.append(current_node.left)

            if current_node.right:
                result.append(current_node.right)

        return max_val


    ################## CC 17 Breadth First Search ##################

    def breadth_first(self, root):
        '''
        Breadth first traversal that takes in binary tree, 
        traverses the tree using breadth first method and finally
        returns a list of the values in order    
        '''
        
        queue = []
        lst = []
        queue.append(root)

        if root is None:
            return 'Tree is empty, nothing to look for...'
    
        while len(queue) > 0:
        
            lst.append(queue[0].value)
            node = queue.pop(0)
    
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return lst



if __name__ == "__main__":

    bt = Binary_Tree()
    bt.root = TNode(5)
    bt.root.left = TNode(4)
    bt.root.right = TNode(14)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(-1)
    bt.root.right.left = TNode(16)
    bt.root.right.right = TNode(20)
    print(bt.pre_order())
    print('\n\n************')
    print(bt.in_order())
    print('\n\n************')
    print(bt.post_order())
    print('\n\n************')
    print(bt.find_maximum_value(bt.root))
    print('\n\n************')
    print(bt.breadth_first(bt.root))

