# -*- coding: utf-8 -*-


from typing import List


def carry(n: int, digits: List[int]) -> List[int]:
    '''Integer carry.
    Args:
        n     : Size of digits.
        digits: List of numbers. [0, digit, ..., digit]
    returns: 
        List of numbers.
    Landau notation: O(n)
    '''

    for pos in range(n - 1, 0, -1):
        p, q = divmod(digits[pos], 10)
        digits[pos] = q
        digits[pos - 1] += p
        
    if digits[0] == 0:
        digits = digits[1:]

    return digits 


def main():
    import sys

    input = sys.stdin.readline
    
    x = input().rstrip()
    n = len(list(x))
    summed = 0
    y = list()

    for xi in x:
        summed += int(xi)
        y.append(summed)
    
    result = carry(n, y)
    print(''.join(map(str, result)))


if __name__ == "__main__":
    main()
