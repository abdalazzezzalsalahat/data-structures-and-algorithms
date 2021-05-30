from tree.tree import Binary_Tree, TNode
from tree.binary_search_tree import Binary_Search_Tree
import pytest

@pytest.fixture
def fixture_tree():
    tree = TNode(1)
    tree.left = TNode(42)
    tree.right = TNode(101)
    tree.left.left = TNode(41)
    tree.right.left = TNode(999)
    b_tree = Binary_Tree(tree)
    return b_tree

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

def test_success_instantiate_an_empty_tree():  ## 1
    ''' Can successfully instantiate an empty tree '''

    tree = Binary_Tree()
    assert tree.root == None

def test_success_instantiate_tree_with_root_node(): ## 2
    ''' Can successfully instantiate a tree with a single root node '''

    tree = Binary_Tree(88)
    assert tree.root == 88

def test_success_left_right_child(): ## 3
    ''' Can successfully add a left child and right child to a single root node '''

    tree = TNode(88)
    tree.left = TNode(42)
    tree.right = TNode(22)

    assert tree.left.value == 42
    assert tree.right.value == 22

def test_success_return_collection_pre_order(fixture_tree): ## 4
    ''' Can successfully return a collection from a pre_order traversal '''
    
    result = fixture_tree.pre_order()
    assert result == [1, 42, 41, 101, 999] 

def test_success_return_collection_post_order(fixture_tree): ## 5
    ''' Can successfully return a collection from an post_order traversal '''

    result = fixture_tree.post_order()
    assert result == [41, 42, 999, 101, 1]

def test_success_return_collection_in_order(fixture_tree): ## 6
    ''' Can successfully return a collection from an inorder traversal '''

    result = fixture_tree.in_order()
    assert result == [41, 42, 1, 999, 101]

def test_success_add_node_to_bst(bst): ## 7
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

def test_success_bst_contains_value(bst): ## 8
    ''' Test for successful traversal of Binary Search Tree to find existance of value '''
    bst.add(1000)
    bst.add(10000)
    bst.add(-1)
    assert bst.contains(1000) == True
    assert bst.contains(10000) == True
    assert bst.contains(-5) == False
    assert bst.contains(-1) == True
    assert bst.contains(99) == False 

############################################# Sunday Max Binary Tree Value ###################################

@pytest.mark.skip
def test_max_value():
    tree = TNode(1)
    tree.left = TNode(42)
    tree.right = TNode(101)
    tree.left.left = TNode(41)
    tree.right.left = TNode(999)
    result = Binary_Tree.find_maximum_value(tree)
    assert result == 999


@pytest.mark.skip
def test_return_max_single_node():

    tree = Binary_Tree(15)
    actual = tree.find_maximum_value_iterative()
    expected = 15
    assert actual == expected
    
@pytest.mark.skip
def test_return_maxVal_of_all(fixture_tree):
    
    actual = tree.find_maximum_value_iterative()
    expected = 999
    assert actual == expected

@pytest.mark.skip
def test_max_of_none():
    '''this test if the binary tree is empty , so the maximum value will be 0 or none'''
    tree = Binary_Tree()
    actual = tree.find_maximum_value_iterative()
    expected = 0

    assert actual == expected

