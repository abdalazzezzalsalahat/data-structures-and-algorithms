def merge_sort(arr):
    '''Takes in a list and sorts list in place'''
    n = len(arr)

    if n > 1:
        
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        
        merge_sort(right)
        
        merge(left, right, arr)

def merge(left, right, arr):
    """[summary]
    Functions as helper function for merge_sort(), doing the actual sorting.

    Args:
        left ([type]): [description]
        right ([type]): [description]
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """
    lft_in, rit_in, arr_i = 0, 0, 0

    while lft_in < len(left) and rit_in < len(right):

        if left[lft_in]  <=  right[rit_in]:

            arr[arr_i] = left[lft_in]
            lft_in += 1

        else:
            arr[arr_i] = right[rit_in]
            rit_in += 1

        arr_i += 1

    if lft_in == len(left):

        for item in right[rit_in:]:

            arr[arr_i] = item
            arr_i += 1
    else:
        for item in left[lft_in:]:

            arr[arr_i] = item
            arr_i += 1

    return arr


if __name__ == "__main__":

    arr1 = [20,18,12,8,5,-2]
    arr2 = [5,12,7,5,5,7]
    arr3 = [2,3,5,7,13,11]
    array = [8,4,23,42,16,15]
    merge_sort(array)
    merge_sort(arr1)
    merge_sort(arr2)
    merge_sort(arr3)
    print(f'Sorted array: {array}')
    print(f'Sorted array: {arr1}')
    print(f'Sorted array: {arr2}')
    print(f'Sorted array: {arr3}')

