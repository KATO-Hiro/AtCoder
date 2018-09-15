# -*- coding: utf-8 -*-


def is_prime(number: int) -> bool:
    '''
        See:
        https://qiita.com/srtk86/items/874639e361917e5016d4
    '''

    from math import sqrt

    if number == 1:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def main():
    n = int(input())
    digit = int(str(n)[-1])

    if is_prime(n):
        print('Prime')
    elif digit % 2 != 0 and digit != 5 and sum(map(int, list(str(n)))) % 3 != 0 and n != 1:
        print('Prime')
    else:
        print('Not Prime')


if __name__ == '__main__':
    main()
