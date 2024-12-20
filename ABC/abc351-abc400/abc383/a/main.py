# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0
    prev = -1

    for i in range(n):
        ti, vi = map(int, input().split())

        if i != 0:
            ans -= ti - prev

        if ans < 0:
            ans = 0

        ans += vi
        prev = ti

    print(ans)


if __name__ == "__main__":
    main()
