from merge_sort.merge_sort import merge_sort, merge
import pytest


def test_empty_list(): ## 1
    '''Test that empty list is handled correctly'''
    array = []
    merge_sort([])
    expected = []
    assert array == expected

def test_one_item_list(): ## 2
    '''Test that single list item is handled correctly'''
    array = [5]
    merge_sort(array)
    expected = [5]
    assert array == expected

def test_two_item_list(): ## 3
    '''Test that list with two items is handled correctly'''
    array = [5,2]
    merge_sort(array)
    expected = [2,5]
    assert array == expected

def test_many_item_list(): ## 4
    '''Test that normal list is handled correctly'''
    array = [8, 20, 18, 5, -2]
    merge_sort(array)
    expected = [-2, 5, 8, 18, 20]
    assert array == expected

