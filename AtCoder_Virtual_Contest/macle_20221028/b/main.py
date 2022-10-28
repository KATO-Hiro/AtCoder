# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    alpha = min([int(input()) for _ in range(5)])
    ans = 5 + ceil(n / alpha) - 1
    print(ans)


if __name__ == "__main__":
    main()
