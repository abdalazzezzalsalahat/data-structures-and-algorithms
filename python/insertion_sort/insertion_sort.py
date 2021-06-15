def insertion_sort(array):
    """[summary]
    A simple sorting algorithm that works similar to the way you sort playing cards in your hands.
    The array is virtually split into a sorted and an unsorted part.
    Values from the unsorted part are picked and placed at the correct position in the sorted part.
    Args:
        array ([list]): [unsorted list]

    Returns:
        [list]: [sorted list]
    """
    for i in range(len(array)):
        index = i - 1
        temp = array[i]

        while index >= 0 and temp < array[index]:
            array[index + 1] = array[index]
            index -= 1

        array[index + 1] = temp
        print(array)
    return array


if __name__ == "__main__":
    arr = [20,18,12,8,5,-2]

    print(insertion_sort(arr))

