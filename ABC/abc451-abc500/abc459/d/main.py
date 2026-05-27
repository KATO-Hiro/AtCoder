# -*- coding: utf-8 -*-

from collections import Counter
from itertools import pairwise


def solve():
    s = input().rstrip()
    n = len(s)
    c = Counter(s)
    d = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
    keys = list(d.keys())

    for value in d.values():
        if value * 2 > (n + 1):
            return False, None

    ans = [""] * n
    pos = 0

    for i in range(0, n, 2):
        key = keys[pos]

        if c[key] == 0:
            pos += 1
            key = keys[pos]

        ans[i] = key
        c[key] -= 1

    for i in range(1, n, 2):
        key = keys[pos]

        if c[key] == 0:
            pos += 1
            key = keys[pos]

        ans[i] = key
        c[key] -= 1

    for first, second in pairwise(ans):
        if first == second:
            return False, None

    return True, "".join(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ok, ans = solve()

        if ok:
            print("Yes")
            print(ans)
        else:
            print("No")


if __name__ == "__main__":
    main()
