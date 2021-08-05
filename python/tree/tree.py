from typing import Counter
from stacks_and_queues.stacks_and_queues import Queue
from collections import deque
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
    #################### Magic functions ####################

    def __init__(self, root = None):
        self.root = root

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __getItem__(self):
        pass

    def __SetItem__(self):
        pass

    def __next__(self):
        pass

    def __next__(self):
        pass

    def __next__(self):
        pass



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

    
    
    ################## final exam trainig ##################

    def ancestors (self, k): ## Recursion
        """[summary]
            a function that is no need for but it is there anyway
        Args:
            k ([type]): [description]

        Returns:
            [type]: [description]
        """

        ance = []
        ance.append(self.root.value)
    
        def walk (root):
        
            if root.left:
                ance.append(root.left.value)
                walk(root.left)
        
            if root.right:
                ance.append(root.right.value)
                walk(root.right)
        
        walk(self.root)
        print(ance)
        if ance[k] in ance:
            return ance[k]
        
        else:
            return -1

    def mergeTrees(self, root_one, root_two): ## Recursion
        """[summary]

        Args:
            root_one ([type]): [description]
            root_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        lst = []
        def walk(r1, r2):
            
            if not r1: 
                lst.append(r2)
            
            if not r2: 
                lst.append(r1)
            
            r1.value += r2.value

            r1.left = walk(r1.left, r2.left)
            r1.right = walk(r1.right, r2.right)
            return lst

        
        return walk(root_one.root, root_two.root)

    def invertTree(self, root): ## Recursion
        """[summary]

        Args:
            root ([type]): [description]

        Returns:
            [type]: [description]
        """
        if root is None:
            return root
        left = root.left
        right = root.right
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root

    def maxDepth(self, root): ### BFS 
        """[summary]

        Args:
            root ([type]): [description]

        Returns:
            [type]: [description]
        """
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 0
        
        while len(q) > 0:
            depth+=1
            tmp = []
            
            for node in q:
                
                if node.left:
                    tmp.append(node.left)
                
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return depth

    def hasPathSum(self, root, targetSum: int) -> bool: ## Recursion
        """[summary]

        Args:
            root ([type]): [description]
            targetSum (int): [description]

        Returns:
            bool: [description]
        """
        def walk(root, tar):
            if(root):
                tar-=root.val
            else:
                return None
            if not tar and (not root.left and not root.right):
                return True
            else:
                return walk(root.left,tar) or walk(root.right,tar)
        return walk(root, targetSum)

    def isSymmetric(self, root) -> bool: ## Recursion
        """[summary]

        Args:
            root ([type]): [description]

        Returns:
            bool: [description]
        """
        def check(left_root, right_root):
            
            if  not left_root and not right_root:
                return True
            
            elif not left_root and right_root: 
                return False 
            
            elif left_root and not right_root:
                return False
            
            else: 
                if left_root.value == right_root.value:
                    return check(left_root.left, right_root.right) and check(left_root.right, right_root.left)
                    
        return check(root.left, root.right)

    def sumOfLeftLeaves(self, root) -> int: ## BFS
        """[summary]

        Args:
            root ([type]): [description]

        Returns:
            int: [description]
        """
        total = 0 
        que = deque([(root, False)])
        
        while que: 
            curr, lefter = que.popleft()

            if not curr.left and not curr.right and lefter: 
                total += curr.value
                
            if curr.left: 
                que.append((curr.left, True))
                
            if curr.right: 
                que.append((curr.right, False))
            
        return total 

    def isSubtree(self, root, subRoot) -> bool: ## Recursion I took this in my final
        """[summary]

        Args:
            root ([type]): [description]
            subRoot ([type]): [description]

        Returns:
            bool: [description]
        """
        if not root:
            return False
        
        def walk(root1,root2):
            
            if not root1 and not root2:
                return True
            
            if (root1 and not root2) or (not root1 and root2):
                return False
            
            if root1.value != root2.value:
                return False
            
            return walk(root1.left,root2.left) and walk(root1.right,root2.right)
        
        if not walk(root,subRoot):
            
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        return True







if __name__ == "__main__":

    bt = Binary_Tree()
    bt.root = TNode(5)
    bt.root.left = TNode(4)
    bt.root.right = TNode(14)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(-51)
    bt.root.right.left = TNode(16)
    bt.root.right.right = TNode(20)

    brr = Binary_Tree()
    brr.root = TNode(5)
    brr.root.left = TNode(7)
    brr.root.right = TNode(3)
    brr.root.left.left = TNode(2)
    brr.root.left.right = TNode(51)
    brr.root.right.right = TNode(10)

    print(bt.pre_order())
    print('\n\n************')
    print(bt.in_order())
    print('\n\n************')
    print(bt.post_order())
    print('\n\n************')
    print(bt.find_maximum_value(bt.root))
    print('\n\n************')
    print(bt.breadth_first(bt.root))
    print('\n\n************')
    print(bt.ancestors(3))
    print('\n\n************')
    print(bt.mergeTrees(bt, brr))



