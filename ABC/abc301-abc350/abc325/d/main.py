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

    input = sys.stdin.readline

    n = int(input())
    lr = []

    for _ in range(n):
        ti, di = map(int, input().split())
        lr.append((ti, ti + di))

    # Greedy
    lr.sort()

    hq = DeletableHeapq()
    i, t = 0, 0
    ans = 0

    while i < n or hq.q:
        # li <= tである限り、キューにriを追加
        while i < n:
            li, ri = lr[i]

            if li > t:
                break

            hq.push(ri)
            i += 1

        # hq.top < tである限り、キューから削除
        while hq.q and hq.top() < t:
            hq.pop()

        # キューに要素が残っているなら答えに+1、要素を削除
        if hq.q:
            ans += 1
            hq.pop()

        # キューが空なら、tを進める
        if i < n and not hq.q:
            lj, _ = lr[i]
            t = lj
        else:
            t += 1

    print(ans)


if __name__ == "__main__":
    main()
