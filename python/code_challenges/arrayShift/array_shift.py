import math

def insertShiftArray(arr, num):
    if len(arr)%2 == 0:
        mid = len(arr) // 2
    else:
        mid = len(arr) // 2 + 1    
    arr[mid:mid] = [num]
    return arr
