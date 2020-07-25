import math
# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:
        return -1

    middle = math.ceil((start + end) / 2)

    if arr[middle] == target:
        return middle

    elif arr[middle] < target:
        start = middle + 1

    elif arr[middle] > target:
        end = middle - 1

    return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    if len(arr) == 0:
        return -1

    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1

    is_desc = True if arr[0] > arr[len(arr) - 1] else False

    middle = math.floor(len(arr) / 2)

    if arr[middle] == target:
        return middle

    if is_desc:
        if arr[middle] < target:
            found_index = agnostic_binary_search(arr[:middle], target)
            return found_index
        else:
            found_index = agnostic_binary_search(arr[middle:], target)
            if found_index == -1:
                return found_index
            else:
                return middle + found_index

    else:
        if arr[middle] < target:
            found_index = agnostic_binary_search(arr[middle:], target)
            if found_index == -1:
                return found_index
            else:
                return middle + found_index
        else:
            found_index = agnostic_binary_search(arr[:middle], target)
            return found_index
