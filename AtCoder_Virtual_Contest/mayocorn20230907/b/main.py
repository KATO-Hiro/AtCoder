# -*- coding: utf-8 -*-


def main():
    import sys
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    numbers = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            numbers.add(i)
            numbers.add(n // i)

    ans = 10**18

    for i in numbers:
        j = n // i
        ans = min(ans, i + j - 2)

    print(ans)


if __name__ == "__main__":
    main()
