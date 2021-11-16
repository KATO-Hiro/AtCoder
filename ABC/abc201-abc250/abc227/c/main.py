# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = 1
    ans = 0

    while a ** 3 <= n:
        b = a

        while a * (b ** 2) <= n:
            c = n // (a * b)

            if c >= b:
                ans += c - b + 1

            b += 1
        a += 1

    print(ans)


if __name__ == "__main__":
    main()
