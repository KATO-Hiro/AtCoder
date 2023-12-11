# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, k = map(int, input().split())
    total = 0

    for _ in range(n):
        pi, qi = map(int, input().split())
        total += pi * qi

    if total < s:
        total += k

    print(total)


if __name__ == "__main__":
    main()
