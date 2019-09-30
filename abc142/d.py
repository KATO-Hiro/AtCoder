# -*- coding: utf-8 -*-


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
    a, b = map(int, input().split())
    set_a = set()
    set_b = set()

    # KeyInsight:
    # x, yが互いに素であることと，x, yの最大公約数が1であることは同値
    # a, bの約数を計算
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            set_a.add(i)
            set_a.add(a // i)

    for i in range(1, int(b ** 0.5) + 1):
        if b % i == 0:
            set_b.add(i)
            set_b.add(b // i)

    # aとbの公約数を求める
    set_ab = set_a & set_b
    count = 1

    # 素数を計算
    for s in set_ab:
        p = Prime(s)

        if p.is_included():
            count += 1

    print(count)


if __name__ == '__main__':
    main()
