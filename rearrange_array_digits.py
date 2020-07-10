def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # empty list case
    if len(input_list) < 1:
        return 0, 0
    
    number1 = ""
    number2 = ""

    # mergesort the list in reverse order
    sorted_list = merge_sort(input_list)
    
    # loop through the sorted list to form two number with max sum
    for i in range(0, len(sorted_list) - 1, 2):
        number1 += str(sorted_list[i])
        number2 += str(sorted_list[i+1])

    if len(sorted_list) % 2:
        number1 += str(sorted_list[len(sorted_list) - 1])
    
    return int(number1), int(number2)


def merge_sort(input_list):
    # Base case: 1 item
    if len(input_list) <= 1:
        return input_list if input_list[0] is not None else []

    # split input_list in half
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    # recursively continue to split list in half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the split lists
    return merge_list(left, right)


def merge_list(left_list, right_list):
    merged_list = []
    left_index = 0
    right_index = 0

    # apply merge sort concept of sorting in place
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(right_list[right_index])
            right_index += 1
        else:
            merged_list.append(left_list[left_index])
            left_index += 1

    # Add the rest of the remaining list to merged list
    merged_list += left_list[left_index:]
    merged_list += right_list[right_index:]

    return merged_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert sum(output) == sum(solution)

# Test: normal cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test: empty list
test_function([[], []])

# Test: list with None value
test_function([[4, None, 2, 5, 9, 8], [952, 84]])

# print("Finished Testing")
