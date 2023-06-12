# -*- coding: utf-8 -*-


def main():
    import sys
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    ans = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.add(n // i)
            ans.add(i)

    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
