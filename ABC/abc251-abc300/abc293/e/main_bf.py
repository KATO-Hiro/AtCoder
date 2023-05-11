# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, x, m = map(int, input().split())
    ans = 0

    for i in range(x):
        ans += a**i
        ans %= m

    print(ans)


if __name__ == "__main__":
    main()
