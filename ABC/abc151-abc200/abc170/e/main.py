# -*- coding: utf-8 -*-


from heapq import heapify, heappop, heappush
from typing import List, Optional


class DeletableHeapq:
    """Alternatives to ordered set (set) in C++.

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

    input = sys.stdin.readline

    n, q = map(int, input().split())
    g_count = 2 * 10 ** 5
    groups = [DeletableHeapq(descending_order=True) for _ in range(g_count)]
    ab = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        bi -= 1
        ab += [[ai, bi]]

        groups[bi].push(ai)

    equality = DeletableHeapq()

    # Get max value in each group.
    for group in groups:
        if group.q:
            equality.push(group.top())

    ans = list()

    for _ in range(q):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1

        rating, group_id = ab[ci]

        # Remove rating in group_id and max value in group_id of equality.
        equality.erase(groups[group_id].top())
        groups[group_id].erase(rating)

        # Get max value in group ci and add equality.
        if groups[group_id].q:
            equality.push(groups[group_id].top())

        # Update di from ci.
        ab[ci][1] = di

        # Remove max value in group_id of equality.
        if groups[di].q:
            equality.erase(groups[di].top())

        # Get max value in group di and add equality.
        groups[di].push(ab[ci][0])
        equality.push(groups[di].top())

        ans += [equality.top()]

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
