# -*- coding: utf-8 -*-

import typing


# See:
# https://github.com/not522/ac-library-python/blob/master/atcoder/string.py
def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    """
    Reference:
    D. Gusfield,
    Algorithms on Strings, Trees, and Sequences: Computer Science and
    Computational Biology
    """

    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)

    if n == 0:
        return []

    z = [0] * n
    j = 0

    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if j + z[j] < i + z[i]:
            j = i

    z[0] = n

    return z


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    t = s[::-1] + s
    z = z_algorithm(t)

    for i in range(n):
        if z[n + i] != n - i:
            continue

        ans = s
        ans += t[n - i : n]
        print(ans)

        break


if __name__ == "__main__":
    main()
