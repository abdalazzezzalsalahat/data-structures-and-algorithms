def insertion_sort(array):
    for i in range(len(array)):
        index = i - 1
        temp = array[i]

        while index >= 0 and temp < array[index]:
            array[index + 1] = array[index]
            index -= 1

        array[index + 1] = temp
        print(array)
    return array

arr = [20,18,12,8,5,-2]

print(insertion_sort(arr))

