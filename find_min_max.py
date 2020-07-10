import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None
    
    min_value = ints[0]
    max_value = ints[0]

    for value in ints:
        if value < min_value:
           min_value = value

        if value > max_value:
            max_value = value

    return (min_value, max_value)


# Test case: regular values
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

assert get_min_max(l) == (0, 9)

# Test case: empty list
assert get_min_max([]) == None

# Test case: None value
assert get_min_max(None) == None

# Test case: negative values
test = [-1,-4,-2,-55,-7,-3,-26]
assert get_min_max(test) == (-55, -1)

# print("Finished testing")
