# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)

    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
