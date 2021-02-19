# -*- coding: utf-8 -*-


class BIT:
    def __init__(self, size: int) -> None:
        self.size = size
        self._bit = [0 for _ in range(self.size + 1)]

    def add(self, index: int, value: int) -> None:
        while index <= self.size:
            self._bit[index] += value
            index += index & -index

    def sum(self, index) -> int:
        summed = 0

        while index > 0:
            summed += self._bit[index]
            index -= index & -index

        return summed


def main():
    n = int(input())
    a = list(map(int, input().split()))

    bit = BIT(n)
    ans = 0

    for index, ai in enumerate(a, 1):
        bit.add(ai, 1)
        ans += index - bit.sum(ai)

    print(ans)


if __name__ == "__main__":
    main()
