# -*- coding: utf-8 -*-

# See:
# https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
import typing


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class LazySegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
        composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
        id_: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size

        for i in range(self._n):
            self._d[self._size + i] = v[i]

        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size

        for i in range(self._log, 0, -1):
            self._push(p >> i)

        self._d[p] = x

        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size

        for i in range(self._log, 0, -1):
            self._push(p >> i)

        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)

            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e

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

    def apply(
        self,
        left: int,
        right: typing.Optional[int] = None,
        f: typing.Optional[typing.Any] = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size

            for i in range(self._log, 0, -1):
                self._push(p >> i)

            self._d[p] = self._mapping(f, self._d[p])

            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n

            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)

                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right

            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1

                if right & 1:
                    right -= 1
                    self._all_apply(right, f)

                left >>= 1
                right >>= 1

            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)

                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size

        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True

        while first or (left & -left) != left:
            first = False

            while left % 2 == 0:
                left >>= 1

            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2

                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1

                return left - self._size

            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size

        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True

        while first or (right & -right) != right:
            first = False
            right -= 1

            while right > 1 and right % 2:
                right >>= 1

            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1

                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1

                return right + 1 - self._size

            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])

        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    sp = [tuple(map(str, input().split())) for _ in range(n)]
    qs = [int(input()) for _ in range(q)]
    r = [(qi, i) for i, qi in enumerate(qs)]
    r.sort()
    t = [ri for ri, _ in r]

    def op(left, right):
        return max(left, right)

    def mapping(p, x):
        if p is None:
            return x
        else:
            return p

    def composition(p, x):
        if p is None:
            return x
        else:
            return p

    inf = 10**18
    st = LazySegTree(op, -inf, mapping, composition, None, t)
    coef = 1

    for si, pi in sp:
        pi = int(pi)

        if si == "NEGATE":
            coef *= -1
        # See:
        # https://atcoder.jp/contests/past18-open/submissions/64006466
        elif si == "CHMIN":
            if coef == 1:
                pos = st.max_right(0, lambda x: x < pi)
                st.apply(pos, q, pi)
            else:
                pos = st.max_right(0, lambda x: x < -pi)
                st.apply(0, pos, -pi)
        else:
            if coef == 1:
                pos = st.max_right(0, lambda x: x < pi)
                st.apply(0, pos, pi)
            else:
                pos = st.max_right(0, lambda x: x < -pi)
                st.apply(pos, q, -pi)

    ans = [0] * q

    for j, (_, i) in enumerate(r):
        value = st.get(j)
        ans[i] = value * coef

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
