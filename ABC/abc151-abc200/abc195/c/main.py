# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    if n >= 10 ** 15:
        ans += 5 * max(0, n - 10 ** 15 + 1)
        ans += 4 * max(0, 10 ** 15 - 10 ** 12)
        ans += 3 * max(0, 10 ** 12 - 10 ** 9)
        ans += 2 * max(0, 10 ** 9 - 10 ** 6)
        ans += 1 * max(0, 10 ** 6 - 10 ** 3)
    elif n >= 10 ** 12:
        ans += 4 * max(0, n - 10 ** 12 + 1)
        ans += 3 * max(0, 10 ** 12 - 10 ** 9)
        ans += 2 * max(0, 10 ** 9 - 10 ** 6)
        ans += 1 * max(0, 10 ** 6 - 10 ** 3)
    elif n >= 10 ** 9:
        ans += 3 * max(0, n - 10 ** 9 + 1)
        ans += 2 * max(0, 10 ** 9 - 10 ** 6)
        ans += 1 * max(0, 10 ** 6 - 10 ** 3)
    elif n >= 10 ** 6:
        ans += 2 * max(0, n - 10 ** 6 + 1)
        ans += 1 * max(0, 10 ** 6 - 10 ** 3)
    elif n >= 10 ** 3:
        ans += 1 * max(0, n - 10 ** 3 + 1)
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
