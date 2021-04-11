# -*- coding: utf-8 -*-


class BIT:
    """Binary Indexed Tree (Fenwick Tree)
    Args:
        size: List size (greater than 0).
    """

    def __init__(self, size: int):
        self.size = size
        self._bit = [0 for _ in range(self.size + 1)]

    def add(self, index: int, value: int) -> None:
        """Adds value to list with index i.
        Args:
            index: The number of index (1-indexed).
            value: A value
        Landau notation: O(log n)
        """

        while index <= self.size:
            self._bit[index] += value
            index += index & -index

    def sum(self, index) -> int:
        """Calculate the sum of elements from 1 to index.
        Args:
            index: The number of index (1-indexed).
        Returns:
            The sum of elements from 1 to index.
        Landau notation: O(log n)
        """

        summed = 0

        while index > 0:
            summed += self._bit[index]
            index -= index & -index

        return summed


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    q = int(input())
    bits = [BIT(n) for _ in range(26)]

    for index, si in enumerate(s, 1):
        c = ord(si) - ord("a")
        bits[c].add(index, 1)

    for i in range(q):
        query = list(input().split())

        if query[0] == "1":
            iq = int(query[1])
            cq = ord(query[2]) - ord("a")
            si = ord(s[iq - 1]) - ord("a")

            bits[si].add(iq, -1)
            s[iq - 1] = query[2]
            bits[cq].add(iq, 1)
        else:
            lq, rq = int(query[1]), int(query[2])
            ans = 0

            for bit in bits:
                if bit.sum(rq) - bit.sum(lq - 1) > 0:
                    ans += 1

            print(ans)


if __name__ == "__main__":
    main()
