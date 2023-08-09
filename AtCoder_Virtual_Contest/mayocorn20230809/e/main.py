# -*- coding: utf-8 -*-


from collections import defaultdict
from heapq import heappop, heappush


class SumOfTopKth:
    """Sum of the k-th number from the smallest (largest) to the k-th.

    See:
    https://atcoder.jp/contests/abc306/submissions/42339375
    """

    __slots__ = (
        "_summed",
        "_k",
        "_in",
        "_out",
        "_d_in",
        "_d_out",
        "_freq",
        "_ascending_order",
    )

    def __init__(self, k: int, ascending_order=True) -> None:
        self._k = k
        self._summed = 0
        self._in = []
        self._out = []
        self._d_in = []
        self._d_out = []
        self._ascending_order = ascending_order
        self._freq = defaultdict(int)

    def query(self) -> int:
        return self._summed if self._ascending_order else -self._summed

    def add(self, x: int) -> None:
        if not self._ascending_order:
            x = -x

        self._freq[x] += 1
        heappush(self._in, -x)
        self._summed += x
        self._modify()

    def discard(self, x: int) -> None:
        if not self._ascending_order:
            x = -x
        if self._freq[x] == 0:
            return

        self._freq[x] -= 1

        if self._in and -self._in[0] == x:
            self._summed -= x
            heappop(self._in)
        elif self._in and -self._in[0] > x:
            self._summed -= x
            heappush(self._d_in, -x)
        else:
            heappush(self._d_out, x)

        self._modify()

    def set_k(self, k: int) -> None:
        self._k = k
        self._modify()

    def get_k(self) -> int:
        return self._k

    def _modify(self) -> None:
        while self._out and (len(self._in) - len(self._d_in) < self._k):
            p = heappop(self._out)

            if self._d_out and p == self._d_out[0]:
                heappop(self._d_out)
            else:
                self._summed += p
                heappush(self._in, -p)

        while len(self._in) - len(self._d_in) > self._k:
            p = -heappop(self._in)

            if self._d_in and p == -self._d_in[0]:
                heappop(self._d_in)
            else:
                self._summed -= p
                heappush(self._out, p)

        while self._d_in and self._in[0] == self._d_in[0]:
            heappop(self._in)
            heappop(self._d_in)

    def __len__(self) -> int:
        return len(self._in) + len(self._out) - len(self._d_in) - len(self._d_out)

    def __contains__(self, x: int) -> bool:
        if not self._ascending_order:
            x = -x
        return self._freq[x] > 0


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    init = sum(sorted(a[:m])[:k])
    ans = [init]

    # smallest
    s = SumOfTopKth(k, ascending_order=True)
    for i in range(m):
        s.add(a[i])

    for i in range(m, n):
        # print(a[i], a[i - m])
        s.add(a[i])
        s.discard(a[i - m])
        # print(s._freq)
        ans.append(s.query())

    print(*ans)


if __name__ == "__main__":
    main()
