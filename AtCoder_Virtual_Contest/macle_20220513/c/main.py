# -*- coding: utf-8 -*-


from typing import List


def generate_divisors(n: int) -> List[int]:
    '''
    Args:
        n: Int of number (greater than 0).
    Returns:
        List of divisors.
        (When n is less than or equal to 2 * 10 ** 5, the number of elements
         is at most 160.)
    Landau notation: O(√n)
    See:
    https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    '''

    lower_divisors, upper_divisors = [], []
    i = 1

    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)

            if i != n // i:
                upper_divisors.append(n // i)

        i += 1

    return lower_divisors + upper_divisors[::-1]


class Prime:
    '''Represents a snippet for prime numbers.
    '''

    def __init__(self, number):
        self.number = number
        self._values = []

    def is_included(self) -> bool:
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

        if (self.number <= 1) or (isinstance(self.number, float)):
            return False

        for i in range(2, int(sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False

        return True


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    da = generate_divisors(a)
    db = generate_divisors(b)
    dc = set(da) & set(db)
    ans = 1

    for ci in dc:
        p = Prime(ci)
        
        if p.is_included():
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
