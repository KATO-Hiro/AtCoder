# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, n = map(int, input().split())
    ans = 10**18

    for b in range(n + 1):
        a = n - 2 * b

        if a < 0:
            continue

        ans = min(ans, x * a + 2 * y * b)

    print(ans)


if __name__ == "__main__":
    main()
