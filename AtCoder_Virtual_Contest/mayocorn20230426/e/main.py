# -*- coding: utf-8 -*-


import typing


# See:
# https://github.com/not522/ac-library-python/blob/master/atcoder/string.py
def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    '''
    Reference:
    D. Gusfield,
    Algorithms on Strings, Trees, and Sequences: Computer Science and
    Computational Biology
    '''

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

    n = int(input())
    t = input().rstrip()
    former = t[:n]
    latter = t[n:][::-1]
    x = former + latter
    y = latter + former

    # Z algorithmで接頭辞を比較
    z_x = z_algorithm(x)
    z_y = z_algorithm(y)

    for i in range(n):
        # 範囲外参照を防ぐ
        if i > 0 and (z_x[2 * n - i] != i):
            continue

        j = n - i

        if z_y[2 * n - j] != j:
            continue

        print(t[:i] + t[i + n:])
        print(i)
        exit()

    print(-1)


if __name__ == "__main__":
    main()
