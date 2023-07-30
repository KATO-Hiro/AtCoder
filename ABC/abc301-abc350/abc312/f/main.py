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

    n, m = map(int, input().split())
    cans0 = DeletableHeapq()
    cans1, openers = list(), list()
    summed = 0

    # 品物の種類別に入力を受け取る
    for _ in range(n):
        ti, xi = map(int, input().split())

        if ti == 0:
            cans0.push(xi)
            summed += xi
        elif ti == 1:
            cans1.append(xi)
        else:
            openers.append(xi)

    # 缶切りが不要な品物がm個よりも多い場合への対処
    while len(cans0.q) > m:
        value = cans0.pop()
        summed -= value

    # print(summed)

    cans1.sort()
    openers.sort(reverse=True)
    item_count = m
    ans = summed

    # 使用できる缶が多い缶切りを使って、缶切りが必要な缶を使う
    for opener_count in openers:
        item_count -= 1

        if item_count == 0:
            break

        for _ in range(opener_count):
            if len(cans1) == 0:
                break

            tmp = cans1.pop()
            cans0.push(tmp)
            summed += tmp

        while len(cans0.q) > item_count:
            tmp = cans0.pop()
            summed -= tmp

        ans = max(ans, summed)

    # print(cans1, openers)
    print(ans)


if __name__ == "__main__":
    main()
