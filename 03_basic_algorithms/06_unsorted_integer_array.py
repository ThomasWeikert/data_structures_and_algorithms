import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    elif len(ints) == 1:
        return (ints[0], ints[0])
    else:
        # Initialize min and max to first element of list
        min_val = ints[0]
        max_val = ints[0]
        
        # Traverse the list from second element to end
        for i in range(1, len(ints)):
            # Check if current element is smaller than current min_val
            if ints[i] < min_val:
                min_val = ints[i]
            
            # Check if current element is greater than current max_val
            if ints[i] > max_val:
                max_val = ints[i]
        
        return (min_val, max_val)

## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")