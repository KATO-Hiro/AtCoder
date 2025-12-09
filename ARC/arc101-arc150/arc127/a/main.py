# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    base = 1
    digit = 1
    ans = 0

    while base <= n:
        lower, upper = base, base + 1

        while lower <= n:
            count = min(upper, n + 1) - lower
            ans += count

            lower *= 10
            upper *= 10

        base *= 10
        base += 1
        digit += 1

    print(ans)


if __name__ == "__main__":
    main()
