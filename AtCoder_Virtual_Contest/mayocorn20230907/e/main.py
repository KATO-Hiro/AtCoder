# -*- coding: utf-8 -*-

from heapq import heapify, heappop, heappush
from typing import List, Optional


class DeletableHeapq:
    """Alternatives to ordered set (set) in C++.

    Landau notation: O(log(n))

    See:
    https://qiita.com/physharp/items/f9229ab879cac9a944d7
    https://prd-xxx.hateblo.jp/entry/2019/06/24/235844
    """

    def __init__(self, descending_order=False) -> None:
        self.q: List[int] = []  # Body
        self.p: List[int] = []  # For deleting
        self.descending_order = descending_order
        self.sign = -1 if descending_order else 1

    def build(self, a: List[int]) -> None:
        """Build a priority-queue q from an array."""

        if self.descending_order:
            a = [-ai for ai in a]

        self.q = a
        heapify(self.q)

    def push(self, number: int) -> None:
        """Add a number to the priority-queue."""
        heappush(self.q, number * self.sign)

    def erase(self, number: int) -> None:
        """Pseudo-erase a number to the priority-queue."""
        heappush(self.p, number * self.sign)
        self.clean()

    def clean(self) -> None:
        """Remove top elements from q, p."""

        while self.p and self.q[0] == self.p[0]:
            heappop(self.q)
            heappop(self.p)

    def pop(self, exc=None) -> Optional[int]:
        """Pop a top value from the priority-queue."""
        self.clean()

        if self.q:
            return heappop(self.q) * self.sign
        return exc

    def top(self, exc=None) -> Optional[int]:
        """Get a top value from the priority-queue.

        Landau notation: O(1)

        Note:
        descending_order=False: min value.
        descending_order=True : max value.
        """
        self.clean()

        if self.q:
            return self.q[0] * self.sign
        return exc


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    cans = list()
    cans_with_cutter = list()
    cutters = list()

    for _ in range(n):
        ti, xi = map(int, input().split())

        if ti == 0:
            cans.append(xi)
        elif ti == 1:
            cans_with_cutter.append(xi)
        elif ti == 2:
            cutters.append(xi)

    size = len(cans)
    cans = sorted(cans, reverse=True)[: min(size, m)]
    cans_with_cutter = sorted(cans_with_cutter, reverse=True)
    cutters = sorted(cutters, reverse=True)
    hq = DeletableHeapq()
    hq.build(cans)
    d = deque(cans_with_cutter)
    cutter_count = 0
    total = sum(cans)
    ans = total

    for cutter in cutters:
        cutter_count += cutter
        m -= 1

        while cutter_count > 0 and len(d) > 0 and m > 0:
            cutter_count -= 1
            di = d.popleft()
            total += di
            hq.push(di)

            while len(hq.q) > m:
                value_min = hq.top()
                dj = hq.pop(value_min)
                total -= dj

            ans = max(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
