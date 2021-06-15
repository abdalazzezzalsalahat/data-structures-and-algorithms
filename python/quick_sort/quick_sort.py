def swap(arr, current, low):
    """[summary]
    Helper function used to shove values lower than pivot value over to the left

    Args:
        arr ([array]): [array to be sorted]
        current ([int]): [index of the currrent element]
        low ([int]): [index of the smallest element]
    """
    temp = arr[current]
    arr[current] = arr[low]
    arr[low] = temp

def partition(arr, left, right):
    """[summary]
    The point of a pivot value is to select a value, 
    find out where it belongs in the array while moving everything lower than that value
    to the left, and everything higher to the right.
    
    Args:
        arr ([array]): [Unorderd array]
        left ([int]): [Left index of the array]
        right ([int]): [Right index of the array]

    Returns:
        [int]: [the value of the lowest element]
    """
    pivot = arr[right]
    low = left - 1

    for current in range(left, right):

        if arr[current] <= pivot:
            low += 1
            swap(arr, current, low)

    swap(arr, right, low + 1)

    return low + 1

def quick_sort(arr, left=None, right=None):
    """[summary]
    Partition the array by setting the position of the pivot value
    
    Args:
        arr ([array]): [Array to be devided]
        left ([int]): [Left index of the array]. Defaults to None.
        right ([int]): [Right index of the array]. Defaults to None.
    """
    if left == None and right == None:

        left = 0
        right = len(arr) - 1

    if left < right:
        position = partition(arr, left, right)

        quick_sort(arr, left, position - 1)

        quick_sort(arr, position + 1, right)


if __name__ == "__main__":

    arr1 = [20,18,12,8,5,-2]
    arr2 = [5,12,7,5,5,7]
    arr3 = [2,3,5,7,13,11]
    array = [8,4,23,42,16,15]
    quick_sort(array)
    quick_sort(arr1)
    quick_sort(arr2)
    quick_sort(arr3)
    print(f'Sorted array: {array}')
    print(f'Sorted array: {arr1}')
    print(f'Sorted array: {arr2}')
    print(f'Sorted array: {arr3}')

