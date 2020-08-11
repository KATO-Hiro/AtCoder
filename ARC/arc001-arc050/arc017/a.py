# -*- coding: utf-8 -*-
'''Snippets for prime.
Available functions:
- is_prime: Determine whether it is a prime number.
'''


def is_prime(number: int) -> bool:
    '''Determine whether it is a prime number.
    Args:
        number: Int of number (greater than 0).
    Returns:
        True if the input number was prime.
        False if the input number was not prime.
    See:
        https://qiita.com/srtk86/items/874639e361917e5016d4
        https://docs.python.org/ja/3/library/2to3.html?highlight=isinstance#2to3fixer-isinstance
    '''

    from math import sqrt

    if (number <= 1) or (isinstance(number, float)):
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def main():
    n = int(input())

    if is_prime(n):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
