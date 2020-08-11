# -*- coding: utf-8 -*-

'''Snippets for prime.
Available functions:
- is_included: Determine whether it is a prime number.
- generate: Generate a list of prime numbers using sieve of Eratosthenes.
'''


class Prime(object):
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

    def generate(self) -> list:
        '''Generate a list of prime numbers using sieve of Eratosthenes.
        Returns:
            A list of prime numbers that is eqaul to or less than the input
            number.
        Landau notation: O(n log log n)
        See:
            https://beta.atcoder.jp/contests/abc110/submissions/3254947
        '''

        if self._values:
            return self._values

        is_met = [True for _ in range(self.number + 1)]
        is_met[0] = False
        is_met[1] = False

        for i in range(2, self.number + 1):
            if is_met[i]:
                self._values.append(i)

                for j in range(2 * i, self.number + 1, i):
                    is_met[j] = False

        return self._values


def main():
    from itertools import accumulate

    q = int(input())
    max_n = 10 ** 5 + 100
    prime = Prime(max_n)
    primes = prime.generate()
    like_numbers = [0 for _ in range(max_n + 1)]

    for current_prime in primes:
        new_prime = Prime((current_prime + 1) // 2)

        if new_prime.is_included():
            like_numbers[current_prime] = 1

    like_number_count = list(accumulate(like_numbers))

    for i in range(q):
        li, ri = map(int, input().split())
        print(like_number_count[ri] - like_number_count[li - 1])


if __name__ == '__main__':
    main()
