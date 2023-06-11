# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    m = n % 5

    if m <= 2:
        ans = n // 5 * 5
    else:
        ans = (n // 5 + 1) * 5

    print(ans)


if __name__ == "__main__":
    main()
