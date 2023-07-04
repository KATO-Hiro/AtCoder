# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/abc194/submissions/20702049
class BITSet:
    """
    set[i] : 集合のi番目に小さい要素を取得 O(logN)
    len(set) : 要素数 O(1)
    set.add(x) : xを追加 O(logN)
    set.remove(x) : xを削除 O(logN)
    set.mex() : 集合にない最小の非負整数を取得 O(logN)
    """

    def __init__(self, max_value: int) -> None:
        self.max_value: int = max_value + 1
        self.bit = BIT(self.max_value)
        self.contain: list[int] = [0] * self.max_value
        self.size: int = 0

    def __getitem__(self, key):
        return self.bit.bisect_left(key)

    def __len__(self) -> int:
        return self.size

    def add(self, key) -> None:
        if not self.contain[key]:
            self.size += 1
            self.contain[key] = 1
            self.bit.add(key)

    def remove(self, key) -> None:
        if self.contain[key]:
            self.size -= 1
            self.contain[key] = 0
            self.bit.add(key, -1)

    def mex(self) -> int:
        result = 0
        value = k = self.bit.max_bit

        while k:
            key = result + k

            if key <= self.max_value and self.bit.data[key] == k:
                value -= k
                result += k

            k >>= 1

        return result


class BIT:
    """
    bit.add(i, val) : s[i] += val O(logN)
    bit.sum(l, r) : s[l:r+1]の区間和、r指定なしのときs[:l]の区間和 O(logN)
    bit.bisect(val) : s[:i+1] >= valとなる最小のi O(logN)
    """

    def __init__(self, size: int) -> None:
        self.size: int = size + 1
        self.data: list[int] = [0] * self.size
        self.max_bit: int = 1 << self.size.bit_length() - 1

    def add(self, key, value=1) -> None:
        key += 1

        while key < self.size:
            self.data[key] += value
            key += key & -key

    def sum(self, left, right=None) -> int:
        left_result = 0

        while left:
            left_result += self.data[left]
            left -= left & -left

        if right is None:
            return left_result

        right += 1
        right_result = 0

        while right:
            right_result += self.data[right]
            right -= right & -right

        return right_result - left_result

    def bisect_left(self, value) -> int:
        result = 0
        k = self.max_bit

        while k:
            key = result + k

            if key < self.size and self.data[key] < value:
                value -= self.data[key]
                result += k

            k >>= 1

        return result


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    b = BITSet(n)

    for i in range(m):
        b.add(a[i])
        d[a[i]] += 1

    ans = [b.mex()]

    for i in range(m, n):
        d[a[i]] += 1
        d[a[i - m]] -= 1

        if d[a[i]] == 1:
            b.add(a[i])
        if d[a[i - m]] == 0:
            b.remove(a[i - m])

        ans.append(b.mex())

    print(min(ans))


if __name__ == "__main__":
    main()
