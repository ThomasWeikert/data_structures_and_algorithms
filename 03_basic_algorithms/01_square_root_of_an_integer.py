def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError("sqrt() argument must be non-negative")
    if number == 0:
        return 0
    if number == 1:
        return 1

    guess = number // 2
    while guess * guess > number:
        guess = (guess + number // guess) // 2

    return guess


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")