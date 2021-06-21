from tree_intersection.tree_intersection import tree_intersection
from tree_intersection.bst import Binary_Search_Tree
from tree_intersection.tree import Binary_Tree
import pytest



########################################## Fixture functions ##########################################
@pytest.fixture
def frst_tre():
    tree = Binary_Search_Tree(88)
    tree.add(66)
    tree.add(60)
    tree.add(55)
    tree.add(50)
    tree.add(40)
    return tree

@pytest.fixture
def sec_tre():
    tree = Binary_Search_Tree(1000)
    tree.add(900)
    tree.add(850)
    tree.add(800)
    tree.add(50)
    tree.add(40)
    return tree

@pytest.fixture
def thrd_tre():
    tree = Binary_Search_Tree(150)
    tree.add(100)
    tree.add(250)
    tree.add(75)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(300)
    tree.add(500)
    


    return tree

@pytest.fixture
def frth_tre():
    tree = Binary_Search_Tree(42)
    tree.add(100)
    tree.add(600)
    tree.add(15)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(4)
    tree.add(500)
    return tree

##########################################  testing functions  ##########################################

def test_null_tree():
    """[summary]
    Returns empty set if either tree is null (empty) 
    """

    frst_tre, sec_tre = Binary_Tree(), Binary_Tree()
    actual = tree_intersection(frst_tre, sec_tre)
    expected = set()
    assert actual == expected


def test_intersection(frst_tre, sec_tre):
    ''' Test that given two BTs only elements found in both sets are returned. '''
    assert tree_intersection(frst_tre, sec_tre) == {50,40}


def test_null_tree():
    ''' Returns empty set if either tree is null (empty) '''
    thrd_tre, frth_tre = Binary_Tree(), Binary_Tree()
    actual = tree_intersection(thrd_tre, frth_tre)
    expected = set()
    assert actual == expected

def test_intersection(thrd_tre, frth_tre):
    """[summary]
    Test if given two BTs only elements found in both sets are returned.
    Args:
        thrd_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
        frth_tre ([fixture functions]): [fixture functions containing an unordered binary tree]
    """
    assert tree_intersection(thrd_tre, frth_tre) == {100,160,125,175,200,350,500}




