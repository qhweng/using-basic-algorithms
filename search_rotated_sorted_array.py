def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # use the binary search algorithm to find number
    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if input_list[mid] == number:
            return mid

        # edge case of none value
        if input_list[mid] is None:
            input_list[mid] = input_list[mid-1] if mid > 0 else input_list[mid+1]
        
        if number >= input_list[start] and number < input_list[mid]:
            end = mid - 1
        elif input_list[start] > input_list[mid]:
            if number < input_list[start]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            start = mid + 1

    # target number not found
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    assert linear_search(input_list, number) == rotated_array_search(input_list, number)

# Test case: list with regular values
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])

# Test case: empty list
test_function([[], 1])

# Test case: list with None value
test_function([[6, 7, 8, 1, 2, None, 4], 4])

# print("Finished testing")
