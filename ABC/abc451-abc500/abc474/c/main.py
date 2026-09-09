# -*- coding: utf-8 -*-


from collections import defaultdict
from itertools import pairwise
from typing import List

HEAD, TAIL = 0, -1


class DoublyLinkedList:

    def __init__(self, array: List) -> None:
        self.next = defaultdict(int)
        self.prev = defaultdict(int)

        for first, second in pairwise([HEAD] + array + [TAIL]):
            self.next[first] = second
            self.prev[second] = first

    def insert(self, value_left: int, value_mid: int) -> None:
        assert value_left in self.next.keys() and value_left in self.prev.keys()
        assert not value_mid in self.next.keys() and not value_mid in self.prev.keys()

        value_right = self.next[value_left]

        self.next[value_left] = value_mid
        self.next[value_mid] = value_right

        self.prev[value_right] = value_mid
        self.prev[value_mid] = value_left

    def remove(self, value_mid: int) -> None:
        assert value_mid in self.next.keys() and value_mid in self.prev.keys()

        value_left, value_right = self.prev[value_mid], self.next[value_mid]

        self.next[value_left] = value_right
        self.prev[value_right] = value_left

        del self.next[value_mid]
        del self.prev[value_mid]

    def fetch_all_values(self) -> List:
        results = list()
        pos = HEAD

        while self.next[pos] != TAIL:
            results.append(self.next[pos])
            pos = self.next[pos]

        return results


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    d = DoublyLinkedList(p)

    if n == 1:
        print(1)
        exit()

    for _ in range(q):
        ai = int(input())

        d.remove(ai)
        last = d.prev[TAIL]
        d.insert(last, ai)

    ans = d.fetch_all_values()
    print(*ans)


if __name__ == "__main__":
    main()
