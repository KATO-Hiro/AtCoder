# -*- coding: utf-8 -*-


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
    from bisect import bisect_right
    import sys

    input = sys.stdin.readline

    size_max = 10 ** 5
    p = Prime(size_max)
    ps = p.generate()
    like_numbers = list()

    for pi in ps:
        if ((pi + 1) // 2) in ps:
            like_numbers.append(pi)

    q = int(input())

    for i in range(q):
        li, ri = map(int, input().split())
        index_li = bisect_right(like_numbers, li - 1)
        index_ri = bisect_right(like_numbers, ri)
        print(index_ri - index_li)
    

if __name__ == "__main__":
    main()
