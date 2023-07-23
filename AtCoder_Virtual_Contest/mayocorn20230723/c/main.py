# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())
    mod = 2019
    r = min(l + 2019, r)
    ans = float("inf")

    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            ans = min(ans, (i * j) % mod)

    print(ans)


if __name__ == "__main__":
    main()
