from tree.tree import Binary_Tree, TNode
from tree.binary_search_tree import Binary_Search_Tree
import pytest

@pytest.fixture
def fixture_tree():
    bt = Binary_Tree(1)
    bt.root = TNode(5)
    bt.root.left = TNode(4)
    bt.root.right = TNode(14)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(-1)
    bt.root.right.left = TNode(16)
    bt.root.right.right = TNode(20)
    return bt

@pytest.fixture
def bst():
    bst_node = TNode(88)
    bst_node.left = TNode(42)
    bst_node.right = TNode(101)
    bst_node.left.left = TNode(41)
    bst_node.right.left = TNode(999)
    bst = Binary_Search_Tree(bst_node)
    return bst

# # # # # 1) Can successfully instantiate an empty tree

# # # # # 2) Can successfully instantiate a tree with a single root node

# # # # # 3) Can successfully add a left child and right child to a single root node

# # # # # 4) Can successfully return a collection from a preorder traversal

# # # # # 5) Can successfully return a collection from an inorder traversal

# # # # # 6) Can successfully return a collection from a postorder traversal

def test_success_instantiate_an_empty_tree(): ## 1  ## 1
    ''' Can successfully instantiate an empty tree '''

    tree = Binary_Tree()
    assert tree.root == None

def test_success_instantiate_tree_with_root_node(): ## 1 ## 2
    ''' Can successfully instantiate a tree with a single root node '''

    tree = Binary_Tree(88)
    assert tree.root == 88

def test_success_left_right_child(): ## 1 ## 3
    ''' Can successfully add a left child and right child to a single root node '''

    tree = TNode(88)
    tree.left = TNode(42)
    tree.right = TNode(22)

    assert tree.left.value == 42
    assert tree.right.value == 22

def test_success_return_collection_pre_order(fixture_tree): ## 1 ## 4
    ''' Can successfully return a collection from a pre_order traversal '''
    
    result = fixture_tree.pre_order()
    assert result == [5, 4, 2, -1, 14, 16, 20]

def test_success_return_collection_post_order(fixture_tree): ## 1 ## 5
    ''' Can successfully return a collection from an post_order traversal '''

    result = fixture_tree.post_order()
    assert result == [2, -1, 4, 16, 20, 14, 5]

def test_success_return_collection_in_order(fixture_tree): ## 1 ## 6
    ''' Can successfully return a collection from an inorder traversal '''

    result = fixture_tree.in_order()
    assert result == [2, 4, -1, 5, 16, 14, 20]

def test_success_add_node_to_bst(bst): ## 1 ## 7
    ''' Test for successful addition of node to Binary Search Tree '''

    node1 = TNode(1)
    node1.left = TNode(42)
    node1.right = TNode(22)
    node1.left.left = TNode(99)
    node1.right.left = TNode(1)
    bst.add(1000)
    bst.add(10000)
    assert bst.root.right.right.value == 1000
    assert bst.root.right.right.right.value == 10000

def test_success_bst_contains_value(bst): ## 1 ## 8
    ''' Test for successful traversal of Binary Search Tree to find existance of value '''
    bst.add(1000)
    bst.add(10000)
    bst.add(-1)
    assert bst.contains(1000) == True
    assert bst.contains(10000) == True
    assert bst.contains(-5) == False
    assert bst.contains(-1) == True
    assert bst.contains(99) == False 

############################################# Sunday CC 16 Max Binary Tree Value #############################################

# @pytest.mark.skip
def test_max_value(fixture_tree): ## 2 ## 1 

    actual = fixture_tree.find_maximum_value(fixture_tree)
    assert actual == 20

# @pytest.mark.skip
def test_max_of_none(): ## 2 ## 4 
    tree = Binary_Tree()
    actual = tree.find_maximum_value()
    expected = 0
    assert actual == expected

############################################# Monday CC 17 Breadth First Search #############################################

def test_empty_tree(): ## 3 ## 1 
    '''If tree is empty  return None.'''
    tree = Binary_Tree()
    actual = tree.breadth_first(tree.root)
    expected = 'Tree is empty, nothing to look for...'
    assert expected == actual

def test_single_tree_node(): ## 3 ## 2
    '''Test that binary tree with single item returns list with that single item.'''
    tree = Binary_Tree()
    tree.root = TNode(15)
    actual = tree.breadth_first(tree.root)
    expected = [15]
    assert expected == actual

def test_a_bunch_tree_nodes(): ## 3 ## 3 
    '''Test that binary tree with four nodes returns list with those a bunch of items.'''

    bt = Binary_Tree()
    bt.root = TNode(2)
    bt.root.left = TNode(7)
    bt.root.right = TNode(5)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(6)

    actual = bt.breadth_first(bt.root)
    expected = [2,7,5,2,6]
    assert expected == actual 

def test_many_tree_nodes(): ## 3 ## 4 
    '''Test that binary tree with 10 nodes returns list with those 10 items.'''
    
    bt = Binary_Tree()
    bt.root = TNode(2)
    bt.root.left = TNode(7)
    bt.root.right = TNode(5)
    bt.root.left.left = TNode(2)
    bt.root.left.right = TNode(6)
    bt.root.right.right = TNode(9)
    bt.root.left.right.left = TNode(5)
    bt.root.left.right.right = TNode(11)
    bt.root.right.right.left = TNode(4)
    actual = bt.breadth_first(bt.root)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert expected == actual   

