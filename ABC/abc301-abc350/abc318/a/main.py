# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, p = map(int, input().split())
    ans = 0

    for i in range(n + 1):
        if m + i * p <= n:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
