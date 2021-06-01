from tree.tree import *
from k_ary_tree.k_ary_tree import *
from tree.binary_search_tree import *

def fizz_buzz_tree(tree):
    '''  which takes a k-ary tree as an argument 
    determine whether or not the value of each node is
     divisible by 3, 5 or both. Create a new tree with the same structure as the original'''
    new_tree = Binary_Tree()
    new_node = TNode()

    if tree.root == None:
        return new_tree
        
    old_node = tree.root

    def visit_node(old_node, new_node):

        new_node.value = fizz_buzz(old_node.value)
        if old_node.left:
            new_node.left = TNode()
            visit_node(old_node.left, new_node.left)

        if old_node.right:
            new_node.right = TNode()
            visit_node(old_node.right, new_node.right)

    def fizz_buzz(old_value):

        result = ''
        if old_value % 3 == 0:
            result += 'Fizz'

        if old_value % 5 == 0:
            result += 'Buzz'

        return result or str(old_value)

    visit_node(old_node, new_node)

    new_tree.root = new_node

    return new_tree

