# I have mintiod two ways to do a binary search. 
# You might not need the first because it's a bit advance
# But I think the second would show that I understand how it works



from bisect import bisect_left

def BinarySearch_fromImport(arr, key):
    '''
    this function calls another outer function called bisect_left
    that divides a sorted list into two halves and check the imported function result
    return the index if key was found or (-1) if not.
    Its formal call is bisect_left(arr, key, lo=0, hi=len(arr))
    not to forget to mintion that it will automatically sort the list ascending
    '''
    index = bisect_left(arr, key)
    if index != len(arr) and arr[index] == key:
        return index
    else:
        return -1



################################  The Second way  #######################################
# In the whiteboard I will be discribing the Second function.

def BinarySearch(arr, key):
    '''
    this function will loop throigh the list 
    and divides it into two halves to check for the key index 
    and return it if it finds it or return (-1) if not.
    '''
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low)
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1