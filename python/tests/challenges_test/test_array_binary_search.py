from code_challenges.array_binary_search.array_binary_search import BinarySearch_fromImport, BinarySearch


# the first function test

def test_first(): ## 1 ## 1
    actual = BinarySearch_fromImport([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_second(): ## 1 ## 2
    actual = BinarySearch_fromImport([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

def test_third(): ## 1 ## 3
    actual = BinarySearch_fromImport([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected

def test_forth(): ## 1 ## 4
    actual = BinarySearch_fromImport([11,22,33,44,55,66,77], 77)
    expected = 6
    assert actual == expected

###############################################################################

# the Second function test

def test_first(): ## 2 ## 1
    actual = BinarySearch([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_second(): ## 2 ## 2
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

def test_third(): ## 2 ## 3
    actual = BinarySearch([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected

def test_forth(): ## 2 ## 4
    actual = BinarySearch([11,22,33,44,55,66,77], 77)
    expected = 6
    assert actual == expected

