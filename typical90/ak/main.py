# -*- coding: utf-8 -*-


import typing


# See:
# ac-library-python
# https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
def _ceil_pow2(n: int) -> int:
    x = 0

    while (1 << x) < n:
        x += 1

    return x


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x

        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1

            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)

            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e
        first = True

        while first or (left & -left) != left:
            first = False

            while left % 2 == 0:
                left >>= 1

            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2

                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size

            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True

        while first or (right & -right) != right:
            first = False
            right -= 1

            while right > 1 and right % 2:
                right >>= 1

            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size

            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


def main():
    import sys

    input = sys.stdin.readline

    w, n = map(int, input().split())
    l, r, v = [0] * n, [0] * n, [0] * n

    for i in range(n):
        li, ri, vi = map(int, input().split())
        l[i], r[i], v[i] = li, ri, vi
    
    w_max = 10 ** 4 + 10
    dp1 = [-1] * (w_max)
    dp1[0] = 0
    st1 = SegTree(max, -1, [-1] * (w_max))
    st1.set(0, 0)

    for i in range(1, n + 1):
        li, ri, vi = l[i - 1], r[i - 1], v[i - 1]
        dp2 = [-1] * (w_max)

        for j in range(w + 1):
            dp2[j] = dp1[j]

            pre_l = max(0, j - ri)
            pre_r = max(0, j - li + 1)

            if pre_l == pre_r:
                continue

            max_value = st1.prod(pre_l, pre_r) # 区間の最大値を取る

            if max_value == -1:
                continue

            dp2[j] = max(max_value + vi, dp1[j])
        
        # 区間の最大値を更新
        for j in range(w + 1):
            st1.set(j, dp2[j])
        
        dp1 = dp2

    ans = dp1[w]

    if ans == -1:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
