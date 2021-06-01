from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
from tree.tree import Binary_Tree, TNode
import pytest

@pytest.fixture
def empty_tree():

    return Binary_Tree()

@pytest.fixture
def fizzy_tree():
    ## preparing data
    bt = Binary_Tree()
    bt.root = TNode(3)
    bt.root.left = TNode(5)
    bt.root.right = TNode(7)
    bt.root.left.left = TNode(15)
    return bt

def test_empty_tree(empty_tree): ## 1

    expected = None
    actual = fizz_buzz_tree(empty_tree)
    assert expected == actual.root
        
def test_fizz_value(fizzy_tree): ## 2

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.value == 'Fizz'
    
def test_buzz_value(fizzy_tree): ## 3

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.left.value == 'Buzz'
    
def test_invalid_value(fizzy_tree): ## 4

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.right.value == '7'
    
def test_both_fizz_buzz_value(fizzy_tree): ## 5

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.left.left.value == 'FizzBuzz'


