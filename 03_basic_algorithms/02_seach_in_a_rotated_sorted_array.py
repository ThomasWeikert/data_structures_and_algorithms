def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # find the pivot element (the smallest element) in the array
    left, right = 0 , len(input_list) - 1
    while left < right:
        mid = (left + right) // 2
        if input_list[mid] > input_list[right]:
            left = mid + 1
        else: 
            right = mid

    # determine which half of the array to search based on the target (number) element
    pivot = left
    left, right = 0 , len(input_list) - 1
    if number >= input_list[pivot] and number <= input_list[right]:
        left = pivot
    else: 
        right = pivot

    # perform binary search on the selected half of the array
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] < number:
            left = mid + 1
        else:
            right = mid -1

    return -1  # the number element is not in the array

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])