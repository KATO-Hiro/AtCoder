# -*- coding: utf-8 -*-


class Prime:
    '''Represents a snippet for prime numbers.
    '''

    def __init__(self, number):
        self.number = number
        self._values = []

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
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = Prime(n)
    print(*sorted(p.generate()))


if __name__ == "__main__":
    main()
