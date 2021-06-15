from quick_sort.quick_sort import quick_sort
import pytest


def test_empty_list(): ## 1
    """[summary]
    Test if empty list is handled correctly
    """
    lst = []
    quick_sort(lst)
    expected = []
    assert lst == expected

def test_repeated_items(): ## 2
    """[summary]
    Test if repeated elemnts list is handled correctly
    """
    lst = [5, 12, 7, 5, 5, 7]
    quick_sort(lst)
    expected = [5, 5, 5, 7, 7, 12]
    assert lst == expected

def test_big_list(): ## 3
    """[summary]
    Test if a big list is handled correctly
    """
    lst = [8, 4, 23, 42, 16, 15, 20, 18, 12, 8, 5, -2]
    quick_sort(lst)
    expected = [-2, 4, 5, 8, 8, 12, 15, 16, 18, 20, 23, 42]
    assert lst == expected

def test_negative_item_list(): ## 4
    """[summary]
    Test if nigative values list is handled correctly
    """
    lst = [20, 18, 12, -8, 5, -2]
    quick_sort(lst)
    expected = [-8, -2, 5, 12, 18, 20]
    assert lst == expected


    