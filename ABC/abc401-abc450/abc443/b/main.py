# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    count = 2 * k + n * (n - 1)
    x = 0

    while True:
        if x * (x + 1) >= count:
            break

        x += 1

    ans = x - n
    print(ans)


if __name__ == "__main__":
    main()
