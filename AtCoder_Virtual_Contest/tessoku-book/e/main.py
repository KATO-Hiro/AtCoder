# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ans = 0

    for red in range(1, n + 1):
        for blue in range(1, n + 1):
            white = k - (red + blue)

            if 1 <= white <= n:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
