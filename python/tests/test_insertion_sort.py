from insertion_sort.insertion_sort import insertion_sort
import pytest


def test_unsorted():  ## 1
    '''Test unsorted array'''
    unsorted_array = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    assert insertion_sort(unsorted_array) == expected

def test_reverse_sorted():  ## 2
    '''Test reversed sort array'''
    reverse_sorted = [20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    assert insertion_sort(reverse_sorted) == expected

def test_few_uniques():  ## 3
    '''Test array with duplicates'''
    few_uniques = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    assert insertion_sort(few_uniques) == expected

def test_nearly_sorted():  ## 4
    '''Test nearly sorted array'''
    nearly_sorted = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    assert insertion_sort(nearly_sorted) == expected

