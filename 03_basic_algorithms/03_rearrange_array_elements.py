def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort the input list using merge sort in descending order
    sorted_list = merge_sort(input_list, reverse=True)

    # Divide the sorted list into two equal parts
    part1 = sorted_list[::2]
    part2 = sorted_list[1::2]

    # Convert each part into a number by concatenating the digits
    num1 = int(''.join(map(str, part1)))
    num2 = int(''.join(map(str, part2)))

    # Return the two numbers as a tuple
    return (num1, num2)


def merge_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, reverse=reverse)
    right = merge_sort(right, reverse=reverse)

    return merge(left, right, reverse=reverse)


def merge(left, right, reverse=False):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (reverse and left[i] > right[j]) or (not reverse and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
