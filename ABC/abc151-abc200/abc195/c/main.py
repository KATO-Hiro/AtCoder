# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, 6):
        ans += max(0, n - (10 ** (3 * i) - 1))

    print(ans)


if __name__ == "__main__":
    main()
