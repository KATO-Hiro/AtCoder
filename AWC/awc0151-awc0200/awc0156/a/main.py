# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(m):
        bi, ci = map(int, input().split())
        bi -= 1

        ai = a[bi]

        if ci > ai:
            continue

        a[bi] -= ci

    print(*a)


if __name__ == "__main__":
    main()
