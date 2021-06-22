from tree_intersection.tree_intersection import tree_intersection
from tree_intersection.bst import Binary_Search_Tree
from tree_intersection.tree import Binary_Tree, TNode
import pytest



########################################## Fixture functions ##########################################
@pytest.fixture
def frst_tre():
    bt = Binary_Tree()
    bt.root = TNode(125)
    bt.root.left = TNode(150)
    bt.root.right = TNode(100)
    bt.root.left.left = TNode(75)
    bt.root.left.right = TNode(350)
    bt.root.right.left = TNode(90)
    bt.root.right.right = TNode(10)
    return bt

@pytest.fixture
def sec_tre():
    bt_two = Binary_Tree()
    bt_two.root = TNode(100)
    bt_two.root.left = TNode(20)
    bt_two.root.right = TNode(75)
    bt_two.root.left.left = TNode(350)
    bt_two.root.left.right = TNode(10)
    bt_two.root.right.left = TNode(35)
    bt_two.root.right.right = TNode(200)
    return bt_two

@pytest.fixture
def thrd_tre():
    bt = Binary_Tree()
    bt.root = TNode(100)
    bt.root.left = TNode(250)
    bt.root.right = TNode(75)
    bt.root.left.left = TNode(160)
    bt.root.left.right = TNode(200)
    bt.root.right.left = TNode(350)
    bt.root.right.right = TNode(125)
    bt.root.right.right.left = TNode(175)
    bt.root.right.right.right = TNode(300)
    bt.root.right.left.left = TNode(500)

    return bt

@pytest.fixture
def frth_tre():
    bt = Binary_Tree()
    bt.root = TNode(100)
    bt.root.left = TNode(600)
    bt.root.right = TNode(15)
    bt.root.left.left = TNode(160)
    bt.root.left.right = TNode(200)
    bt.root.right.left = TNode(350)
    bt.root.right.right = TNode(125)
    bt.root.right.right.left = TNode(175)
    bt.root.right.right.right = TNode(4)
    bt.root.right.left.left = TNode(500)

    return bt

##########################################  testing functions  ##########################################

def test_null_tree(): ## 1
    """[summary]
    Returns empty set if either tree is null (empty) 
    """
    
    thrd_tre, frth_tre = Binary_Tree(), Binary_Tree()
    thrd_tre = thrd_tre.is_empty(thrd_tre.root)
    frth_tre = frth_tre.is_empty(frth_tre.root)
    actual = tree_intersection(thrd_tre, frth_tre)
    expected = "tree is empty"
    assert actual == expected

def test_intersection_first(frst_tre, sec_tre): ## 2
    """[summary]
    Test that given two BTs only elements found in both sets are returned.
    Args:
        frst_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
        sec_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
    """
    assert tree_intersection(frst_tre, sec_tre) == ['100', '350', '10', '75']

def test_intersection_second(thrd_tre, frth_tre): ## 3
    """[summary]
    Test if given two BTs only elements found in both sets are returned.
    Args:
        thrd_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
        frth_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
    """
    assert tree_intersection(thrd_tre, frth_tre) == ['100', '160', '200', '350', '500', '125', '175']

def test_sec_thrd_tree(sec_tre,thrd_tre): ## 4
    """[summary]
    Test that given two BTs only elements found in both sets are returned.
    Args:
        sec_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
        thrd_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
    """
    assert tree_intersection(sec_tre, thrd_tre) == ['100', '200', '75', '350']

