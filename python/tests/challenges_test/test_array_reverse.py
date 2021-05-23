from code_challenges.array_reverse.array_reverse import reverse_array

def test_first(): ## 1
    # arrange
    actual = reverse_array([1, 2, 3, 4, 5, 6])
    # assign
    expected = [6, 5, 4, 3, 2, 1]
    #assert
    assert actual == expected
    
def test_second(): ## 2
    actual = reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12])
    expected = [-12, 823, -923, 10, 23, 3546, 2354, 89]
    assert actual == expected

def test_third(): ## 3
    actual = reverse_array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])
    expected = [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
    assert actual == expected

