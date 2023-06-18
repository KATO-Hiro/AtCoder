# -*- coding: utf-8 -*-


import random
import string
import traceback


# See:
# https://atcoder.jp/contests/abc284/submissions/37841742
class RollingHashWithRange:
    def __init__(self, parent, left, right) -> None:
        self.parent = parent
        self.left = left
        self.right = right

    def __getitem__(self, key):
        if key > self.right - self.left:
            traceback.print_exc()
            raise Exception("index out of range")

        return self.get(self.left, self.left + key)

    # Overall hash value
    def get(self, left, right):
        mod = RollingHash.mod
        return (
            self.parent.hash[right]
            - self.parent.hash[left] * self.parent.power[right - left]
        ) % mod

    def __len__(self):
        return self.right - self.left

    def __eq__(self, other):
        return self.get(self.left, self.right) == other.get(other.left, other.right)

    # Longest Common Prefix
    def __lt__(self, other):
        length = min(len(self), len(other))

        if self[length] == other[length]:
            return len(self) < len(other)

        left, right = 0, length

        while True:
            mid = (left + right) // 2

            if left == right:
                return (
                    self.parent.s[self.left + right - 1]
                    < other.parent.s[other.left + right - 1]
                )

            if self[mid] != other[mid]:
                right = mid
            else:
                left = mid + 1
                right = right


class RollingHash:
    base = 30
    mod = 10**9 + 9

    @classmethod
    def config(cls, base, mod) -> None:
        RollingHash.base = base
        RollingHash.mod = mod

    def __init__(self, s) -> None:
        mod = RollingHash.mod
        base = RollingHash.base
        self.power = power = [1] * (len(s) + 1)
        self.s = s

        size = len(s)
        self.hash = hash = [0] * (size + 1)

        value = 0

        for i in range(size):
            hash[i + 1] = value = (value * base + ord(s[i])) % mod

        value = 1

        for i in range(size):
            power[i + 1] = value = value * base % mod

    def get(self, left, right) -> RollingHashWithRange:
        return RollingHashWithRange(self, left, right)


def get_random_name(n):
    rand_list = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return "".join(rand_list)


def test():
    RollingHash.config(100, 10**9 + 7)

    for i in range(100):
        n = 5
        x, y = get_random_name(n), get_random_name(n)
        y = x

        if (x < y) != (RollingHash(x).get(0, n) < RollingHash(y).get(0, n)):
            print(
                "No", x < y, RollingHash(x).get(0, n) < RollingHash(y).get(0, n), x, y
            )


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = input().rstrip()
    rh1 = RollingHash(s)
    rh2 = RollingHash(s[::-1])

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1

        if rh1.get(li, ri) == rh2.get(n - ri, n - li):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
