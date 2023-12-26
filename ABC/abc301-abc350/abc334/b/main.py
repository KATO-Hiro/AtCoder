# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, m, l, r = map(int, input().split())

    lower = (l - a + m - 1) // m
    upper = (r - a) // m

    ans = upper - lower + 1

    print(ans)


if __name__ == "__main__":
    main()
