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

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    hq = [DeletableHeapq() for _ in range(n)]

    def dfs(cur, parent=-1):
        for to in graph[cur]:
            if to == parent:
                continue

            dfs(to, cur)
            # print("foo", cur, to)

            for value in hq[to].q:
                hq[cur].push(value)

            while len(hq[cur].q) > 20:
                min_value = hq[cur].top()
                hq[cur].pop(min_value)

        # print("bar", cur)
        hq[cur].push(x[cur])

        while len(hq[cur].q) > 20:
            min_value = hq[cur].top()
            hq[cur].pop(min_value)

    dfs(0)

    for hi in hq:
        hi.q = sorted(hi.q, reverse=True)
        # print(hi.q)

    for _ in range(q):
        vi, ki = map(int, input().split())
        vi -= 1
        ki -= 1
        print(hq[vi].q[ki])


if __name__ == "__main__":
    main()
