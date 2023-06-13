# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [m] * n

    for ai in a:
        ans[ai - 1] -= 1

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
