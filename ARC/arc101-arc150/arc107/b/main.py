# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    # x = a + b、y = c + d
    # x - y = k
    # x を全探索
    ans = 0

    for x in range(2, 2 * n + 1):
        y = x - k

        if not (2 <= y <= 2 * n):
            continue

        x2 = x - 1 if (x - 1) <= n else (2 * n - x + 1)
        y2 = y - 1 if (y - 1) <= n else (2 * n - y + 1)

        ans += x2 * y2

    print(ans)


if __name__ == "__main__":
    main()
