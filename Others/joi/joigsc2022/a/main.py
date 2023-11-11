# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ba = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        ba.append((bi, ai))

    ba.sort()
    # print(ba)
    inf = 10**18
    first, second, ans = inf, inf, inf

    for i in range(n - 1, -1, -1):
        bi, ai = ba[i]
        ans = min(ans, ai + first + second)

        ci = ai + bi

        if ci < first:
            second = first
            first = ci
        elif ci < second:
            second = ci

    print(ans)


if __name__ == "__main__":
    main()
