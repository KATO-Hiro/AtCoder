# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float("inf")

    for x in range(26):
        for y in range(26):
            diff = n - (8 * x + 10 * y)

            if diff >= 0 and diff % 26 == 0:
                ans = min(ans, x + y)

    print(ans)


if __name__ == "__main__":
    main()
