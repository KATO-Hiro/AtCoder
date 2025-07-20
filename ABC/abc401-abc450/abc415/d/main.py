# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    da = list()

    for _ in range(m):
        ai, bi = map(int, input().split())
        da.append((ai - bi, ai))

    da.sort()
    ans = 0

    for di, ai in da:
        if n < ai:
            continue

        count = (n - ai) // di + 1
        ans += count
        n -= count * di

    print(ans)


if __name__ == "__main__":
    main()
