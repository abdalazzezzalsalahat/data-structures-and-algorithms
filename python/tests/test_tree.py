from tree.tree import BinaryTree, TNode, Binary_Search_Tree
import pytest

@pytest.fixture
def fixture_tree():
    tree = TNode(1)
    tree.left = TNode(42)
    tree.right = TNode(22)
    tree.left.left = TNode(99)
    tree.right.left = TNode(1)
    b_tree = BinaryTree(tree)
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

    tree = BinaryTree()
    assert tree.root == None

def test_success_instantiate_tree_with_root_node(): ## 2
    ''' Can successfully instantiate a tree with a single root node '''

    tree = BinaryTree(88)
    assert tree.root == 88


@pytest.mark.skip
def test_success_left_right_child(): ## 3
    ''' Can successfully add a left child and right child to a single root node '''

    tree = TNode(88)
    tree.left = TNode(42)
    tree.right = TNode(22)

    assert tree.root.left.value == 42
    assert tree.root.right.value == 22

@pytest.mark.skip
def test_success_return_collection_pre_order(fixture_tree): ## 4
    ''' Can successfully return a collection from a pre_order traversal '''
    
    result = fixture_tree.pre_order()
    assert result == [88, 42, 99, 22, 1] 

@pytest.mark.skip
def test_success_return_collection_post_order(fixture_tree): ## 5
    ''' Can successfully return a collection from an post_order traversal '''

    result = fixture_tree.post_order()
    assert result == [99, 42, 1, 22, 88]

@pytest.mark.skip
def test_success_return_collection_in_order(fixture_tree): ## 6
    ''' Can successfully return a collection from an inorder traversal '''
    result = fixture_tree.in_order()
    assert result == [99, 42, 88, 1, 22]

@pytest.mark.skip
def test_success_add_node_to_bst(bst):
    ''' Test for successful addition of node to Binary Search Tree '''

    bst.add(1000)
    bst.add(10_000)
    assert bst.root.left.right.value == 1000
    assert bst.root.right.left.right.value == 10_000

@pytest.mark.skip
def test_success_bst_contains_value(bst):
    ''' Test for successful traversal of Binary Search Tree to find existance of value '''

    bst.add(1000)
    bst.add(10_000)
    bst.add(-1)
    assert bst.contains(1000) == True
    assert bst.contains(10_000) == True
    assert bst.contains(-5) == False
    assert bst.contains(-1) == True
    assert bst.contains(99) == False 


