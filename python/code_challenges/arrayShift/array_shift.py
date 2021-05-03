def insertShiftArray (arr, num):
    for x in range(len(arr)):
        if arr[x] > num:
            i = x
            break
    arr = arr[:x] + [num] + arr[x:]
    return arr
