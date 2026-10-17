# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, k, t = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    flag = False

    if a[0] != 0:
        a = [0] + a
        flag = True

    while a[-1] > t:
        a.pop()

    if a[-1] != t:
        a.append(t)

    ans = 0

    for ai, aj in pairwise(a):
        if ai == 0 and flag:
            ans += ceil(aj, k)
            continue

        ans += ceil(max(0, aj - ai - k), k)

    print(ans)


if __name__ == "__main__":
    main()
