def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base cases
    if number == 1 or number == 0 or number is None:
        return number

    # Negative number cases
    if number < 0:
        return -1

    # Follow binary search algorithm to calculate sqrt
    start = 0
    end = number
    mid = -1

    while start <= end or start == mid:
        mid = (start + end) // 2

        if mid**2 == number:
            return mid

        if mid**2 > number:
            end = mid - 1
        else:
            start = mid + 1

    return mid
    

# Test case: regular values
assert 3 == sqrt(9)
assert 4 == sqrt(16)
assert 0 == sqrt(0)
assert 1 == sqrt(1)

# Test case: values with remainders
assert 5 == sqrt(27)
assert 5 == sqrt(33)
assert 1 == sqrt(2)
assert 1 == sqrt(3)

# Test case: negative value
assert -1 == sqrt(-10)
assert -1 == sqrt(-15)

# Test case: none value
assert None == sqrt(None)

# print("Finished testing")
