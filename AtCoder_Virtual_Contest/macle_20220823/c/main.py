# -*- coding: utf-8 -*-


def count_digit(max_number: int) -> int:
    '''
    Args:
        max_number: Int of number (greater than 1).
    Returns:
        the number of digit.
    Landau notation: O(log n)
    '''
    if max_number == 0:
        return 1

    digit = 0

    while max_number:
        digit += 1
        max_number //= 10

    return digit


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float("inf")

    for i in range(1, int(sqrt(n)) + 1):
        a = n % i
        
        if a == 0:
            b = n // i

            ans = min(ans, max(count_digit(a), count_digit(b)))
    
    print(ans)



if __name__ == "__main__":
    main()
