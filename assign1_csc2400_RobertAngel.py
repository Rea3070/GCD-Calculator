# File: Assign1_csc2400_Angel.py
# Author: Robert Angel
# Date: September 29, 2023,
# Description: This computes GCD using three algorithms.
# License: MIT License

def euclid(a, b) -> tuple:
    """
    Calculates GCD using extended euclid algorithm

    Args:
        int a, b to be calculated.

    Returns:
        tuple: GCD, x, y.
    """
    # Base Case if one is zero, return the other
    if a == 0:
        return b, 0, 1
    if b == 0:
        return a, 0, 1

    # If a number is negative, make it positive since the GCD doesn't change
    if a < 0:
        a = a - a * 2
    if b < 0:
        b = b - b * 2

    # Recursively calculate GCD
    gcd, x1, y1 = euclid(b % a, a)

    # x and y are the numbers you can multiply a and b by to get GCD
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def consecutive_int(a, b) -> int:
    """
    Calculates GCD using consecutive integer algorithm

    Args:
        int a, b to be calculated.

    Returns:
        int: the GCD.
    """

    # Base case if either are zero, return the other number
    if a == 0:
        return b
    if b == 0:
        return a

    # If a number is negative, make it positive since the GCD doesn't change
    if a < 0:
        a = a - a * 2
    if b < 0:
        b = b - b * 2

    # find the smaller of the two numbers
    if a > b:
        i = b
    else:
        i = a

    # Consecutive int algorithm
    while i > 0:
        # If both 'a' and 'b' are divisible by 'small', return 'small' as the GCD
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


# users choice
choice = int(input("Choose algorithm: \n 1. extended euclid \n 2. consecutive int \n"))

# numbers being computed
a, b = [int(x) for x in input("\n\nEnter two values (Enter on the same line, separated by a space): ").split()]

# set GCD to 1 as base case
gcd = 1

# while loop for user menu
while choice > 0:
    match choice:
        case 1:  # Extended Euclid's Algorithm
            gcd, x, y = euclid(a, b)
            match gcd:
                case 0:  # undefined case
                    print("gcd(", a, ",", b, ") = undefined")
                case _:  # default case
                    print("gcd(", a, ",", b, ") = ", gcd)

        case 2:  # consecutive int algorithm
            gcd = consecutive_int(a, b)
            match gcd:
                case 0:  # undefined case
                    print("gcd(", a, ",", b, ") = undefined")
                case _:  # default case
                    print("gcd(", a, ",", b, ") = ", gcd)

    # Re-prompt user for their choice of algorithm
    choice = int(input("\nChoose another algorithm: \n 1. extended euclid \n 2. consecutive int \n 0. quit \n"))

    # Re-Prompt user for numbers to be computed
    if choice > 0:
        a, b = [int(x) for x in input("Enter two values (Enter on the same line, separated by a space): ").split()]
