# Quick Sort Blog

## Discription 
> *QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.*


## Pseudocode

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

```


## Python Implementation 


```
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



```



## Trace

`arr =    [8, 4, 23, 42, 16, 15]`

Indexes:   0  1   2   3   4   5

low = 0,   
high =  5,  
pivot = arr[high] = `15` 
##### i = -1 

Traverse from `j = low` to `high-1`    
j = 0 : Since `arr[j] <= pivot`, do i++ and swap(arr[i], arr[j])
i = 0 

`arr = [8, 4, 23, 42, 16, 15]`
i and j are the same so no change  

j = 1 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 2 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 1  
=> `arr = [4, 8, 23, 42, 16, 15]`  We swap 8 and 4

j = 4 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 5 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 2  

=> `arr = [4, 8, 15, 42, 16, 23]` 23 and 15 swapped


j = 5 : Since `arr[j] <= pivot`, iterate and swap arr[i] with arr[j] 
i = 3   

=> `arr = [4, 8, 15, 16, 42, 23]` 23 and 16 Swapped 


j = 5 : Since `arr[j] <= pivot`, iterate and swap arr[i] with arr[j] 
i = 4  
=> `arr = [4, 8, 15, 16, 23, 42]` 42 and 23 Swapped 

===> `j == high-1`, breaking the loop  

